import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
size = 20
def go():
    midx = int(x + size/2)
    midy = int(y + size/2)
    mc.setBlocks(x, y, z, x + size, y + size, z + size, block.COBBLESTONE.id)
    mc.setBlocks(x + 1, y + 1, z + 1, x + size - 1, y + size -1, z + size - 1, block.AIR.id)
    mc.setBlocks(midx - 1, y, z, midx + 1, y + 3, z, block.DOOR_IRON.id)
    mc.setBlocks(x + 3, y + size - 3, z, midx - 3, midy + 3, z, block.GLASS.id)
    mc.setBlocks(midx + 3, y + size - 3, z, x + size - 3, midy + 3, z, block.GLASS.id)
    mc.setBlocks(x, y + size - 1, z, x + size, y + size - 1, z + size, block.WOOD.id)
    mc.setBlocks(x + 1, y - 1, z + 1, x + size -2, y - 1, z + size -2, block.DIAMOND_BLOCK.id)
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
go()
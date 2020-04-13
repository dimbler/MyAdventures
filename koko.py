import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
while tuple:
    size = 200
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50 + size, pos.y+50 + size, pos.z+50 + size, block.WATER_STATIONARY.id)

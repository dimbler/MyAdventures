import time

from mcpi.minecraf
mc = Minecraft.create()
pos = mc.player.getTilePos()
X1 = 10
Z1 = 10
X2 = 20
Z2 = 20
HOME_X = X2 + 2
HOME_Y = 10
HOME_Z = Z2 + 2
rent = 0
inField = 0
while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.postToChat("X:{} Y:{} Z:{}".format(pos.x, pos.y, pos.z))
    if pos.x > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        rent = rent + 1
        mc.postToChat("You owe rent:" + str(rent))
        inField = inField + 1
    else:
        inField = 0
    if inField >3:
            mc.postToChat("Too slow!")
            mc.player.setPos(HOME_X, HOME_Y, HOME_Z)
from ova import *
import random
import time
import os

robot:IRobot = OvaClientMqtt(id="ova1097bdcb48b1", arena="ishihara", username="epsirennes2023", server="192.168.10.103")

print("🟢 BEGIN TEST")
robot.playMelody([("C4",50),("D4",50),("E4",50),("F4",50),("G4",50)])
robot.setMotorSpeed(0,0)
robot.setLedColor(0,0,0)
robot.update()

os.system('cls')
print("📸 Test camera")
while True:

	sr = 0
	sg = 0
	sb = 0
	n = 0

	color = robot.getImagePixelRGB(robot.getImageWidth() // 2, robot.getImageHeight()-1)
	sr = color[0]
	sg = color[1]
	sb = color[2]
	os.system('cls')
	print("📸 Camera img "+str(robot.getImageWidth())+"x"+str(robot.getImageWidth())+" shot after "+str(robot.getImageTimestamp())+"ms")
	print("🔴<R>="+str(sr)+" 🟢<G>="+str(sg)+" 🔵<B>="+str(sb))
	robot.setLedColor(sr,sg,sb)
	robot.update()

# End
os.system('cls')
print("🔴 END TEST")
endMelody = []
for i in range(10,2,-1):
	endMelody.append((i,50))
robot.playMelody(endMelody)
robot.setMotorSpeed(0,0)
robot.setLedColor(0,0,0)
robot.update()

import serial
import time
import random

ser = serial.Serial('/dev/ttyACM0',115200)

def formatAndSend(stringToFormatAndSend):
    ser.write((stringToFormatAndSend + '\n').encode("utf-8"))

#formatAndSend("4|")
formatAndSend("2|30")
time.sleep(.1)
numLEDs = 144

while True:
    strToSend = "3|"
    loop = 0
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pixels = [ (r,g,b) ] * numLEDs

    for n in pixels:
        strToSend = strToSend + str(loop) + "(" + str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) + ")"
        loop += 1
    #print(strToSend)
    formatAndSend(strToSend)
    #time.sleep(.2)
    
#print(strToSend)

#formatAndSend(strToSend)
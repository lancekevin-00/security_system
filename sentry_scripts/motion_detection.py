#! /usr/bin/python
import RPi.GPIO as GPIO
import os.path
import subprocess
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
file='motion_detected.txt'
try:  
    while True:            # this will carry on until you hit CTRL+C
        if os.path.isfile('on.txt'):  
            if GPIO.input(4): # if port 25 == 1 (motion is detected)
                print "Motion Detected"
                subprocess.call("./camera_control")
                f=open(file, "w")
                f.close()
            else:  
                print "..."
                if os.path.isfile(file): #if motion is not detected delete motion detected.txt
                    os.remove(file)
        sleep(0.1)         # wait 0.1 seconds  
  
finally:
    GPIO.cleanup()

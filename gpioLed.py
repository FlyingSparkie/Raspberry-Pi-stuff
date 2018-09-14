import RPi.GPIO as GPIO             #import the gpio library
from time import sleep              #import time library


redLed=22     #what pin
greenLed=23
blinkTimes=[0,1,2,3,4]
button=17
inputButton=False
range(5)


GPIO.setmode(GPIO.BCM)              #set gpio mode BCM, not BOARD
GPIO.setup(greenLed, GPIO.OUT)     #make it an output
GPIO.setup(redLed, GPIO.OUT)     #make it an output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.output(yellowLed, False)       #turn on(True) off(False)
#GPIO.cleanup()                      #reset the pins
#GPIO.setmode(GPIO.BCM)
#while True:
#    GPIO.output(yellowLed, True)
#    sleep(1)
#    GPIO.output(yellowLed, False)
#    sleep(1)

 #iterate list to blink variable
#for i in blinkTimes:
#    GPIO.output(yellowLed, True)
#    sleep(1)
#    GPIO.output(yellowLed, False)
#    sleep(1)
try:
    
    while True:
       # inputButton=GPIO.input(button)
        #if inputButton==True:
         #   print("Buttun pressed")
            sleep(3)

    #range example
            for i in range(5):
                GPIO.output(greenLed, True)
                sleep(1)
                GPIO.output(greenLed, False)
                sleep(1)
            for i in range(5):
                GPIO.output(greenLed, True)
                sleep(.25)
                GPIO.output(greenLed, False)
                sleep(.25)
            for i in range(3):
                GPIO.output(redLed, True)
                sleep(4)
    GPIO.output(redLed, False)
    sleep(.25)
except KeyboardInterrupt:
    print("Finished")
GPIO.cleanup()

    

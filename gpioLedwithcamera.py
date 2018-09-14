import RPi.GPIO as gpio             #import the gpio library
from time import sleep              #import time library
import picamera


redLed=25     #what pin
greenLed=17
yelled=27
grnled=27
redled2=27
yelled2=27


blinkTimes=[0,1,2,3,4]
button=23
inputButton=False
range(7)


gpio.setmode(gpio.BCM)              #set gpio mode BCM, not BOARD
gpio.setup(greenLed, gpio.OUT)      #make it an output
gpio.setup(redLed, gpio.OUT)        #make it an output
gpio.setup(yelled, gpio.OUT)        #make it an output
gpio.setup(grnled, gpio.OUT)        #make it an output
gpio.setup(yelled2, gpio.OUT)       #make it an output
gpio.setup(redled2, gpio.OUT)       #make it an output
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

camera = picamera.PiCamera()
# camera.resolution=(640,480)
camera.resolution=(320,240)
camera.brightness=60


try:
    print("Waiting for sensor trip")
    while True:
        
       # input_state=gpio.input(button)
        input_state = gpio.input(button)
        if input_state==False:
            print("Taking picture activated")
            sleep(.5)
            for i in range(3):
                gpio.output(greenLed, True)
                sleep(1)
                gpio.output(greenLed, False)
                sleep(1)
            for i in range(3):
                gpio.output(greenLed, True)
                sleep(.25)
                gpio.output(greenLed, False)
                sleep(.25)
            camera.start_preview()
            sleep(1)
            print("Taking.....")
            camera.capture('testimage.jpg')
            camera.stop_preview()
          #  camera.close()
            print ("Image captured")
            
        
            for i in range(7):
                gpio.output(redLed, True)
                sleep(.03)
                gpio.output(redLed, False)
                sleep(.1)
            for i in range(3):
                gpio.output(yelled, True)
                sleep(.2)
                gpio.output(yelled, False)
                sleep(.2)
                gpio.output(redled2, True)
                sleep(.2)
                gpio.output(redled2, False)
                sleep(.2)

            print("Press Ctrl&C once to update website or twice to QUIT")
            #camera.close()
            print("Waiting for sensor trip")
    gpio.cleanup()
    camera.close()
except KeyboardInterrupt:
    gpio.cleanup()
    camera.close()
    print("Now......")
    
    

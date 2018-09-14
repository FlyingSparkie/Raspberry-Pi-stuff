import RPi.GPIO as gpio
from time import sleep
import sys
import pygame
#from pygame import *
#import pygame as e

def keyleft():
	print ("left key press")
	pwm.start(2)
	return()

def keyright():
	print ("right key pressed")
	pwm.start(10)
	return()

def centered():
	print("Centering")
	pwm.start(6)
	return()

gpio.setmode(gpio.BCM)
gpio.setup(22,gpio.OUT)
pwm=gpio.PWM(22,50)
pwm.start(5)
sleep(2)
pwm.start(7.5)
sleep(1)
pwm.start(2)
sleep(2)
#init()


#   while True:
#       inkey = raw_input()
#      if inkey == "z":
#          keyleft()
#      elif inkey == "x":
#          keyright()
#       else:
#          print("All stop")
#          centered()
#   print ("loop finished")

##############################################

#try:
pygame.display.init()
screen = pygame.display.set_mode((320,240))
print("waiting for input")
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_z):
                #keyleft()
                pwm.start(6)
                print("z key pressed")
                #pwm.start(5)
                pwm.start(2)
            elif(event.key == pygame.K_x):
                #keyright()
                pwm.start(6)
                print("x key pressed")
                #pwm.start(5)
                pwm.start(12)
            else:
                #centered()
                print("Centered")
                pwm.start(2)
                #pwm.start(10)
                pwm.start(5)
        
#gpio.cleanup()

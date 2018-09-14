import RPi.GPIO as gpio
from time import sleep

def keyleft():
	print ("left key press")
	pwm.start(1)
	return()

def keyright():
	print ("right key pressed")
	pwm.start(12)
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
sleep(3)
pwm.start(1)
sleep(2)
#pwm.start(10)
#pwm.start(7.5)
#pwm.start(3)

try:
	print("waiting fpr input")
while 1:


	inkey = raw_input()
	if inkey == "z":
		keyleft()
	elif inkey == "x":
		keyright()
	else:
		print("All stop")
		centered()

except KeyboardInterrupt:
print ("loop finished")

gpio.cleanup()

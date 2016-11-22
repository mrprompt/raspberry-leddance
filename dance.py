#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import time
import random
import RPi.GPIO as GPIO

# LEDs GPIO port: 11 = Green, 13 = Gray, 16 = Red
pins = [11, 12, 13, 15, 16, 18]
delay = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

try:
	while True:
		pin = random.choice(pins)

		GPIO.output(pin, GPIO.HIGH)
		time.sleep(delay)

		GPIO.output(pin, GPIO.LOW)
		time.sleep(delay)

except KeyboardInterrupt:
	print("A keyboard interrupt has been noticed")

except Exception, e:
	print("An error or exception has ocurred: " + str(e))

finally:
	GPIO.cleanup()

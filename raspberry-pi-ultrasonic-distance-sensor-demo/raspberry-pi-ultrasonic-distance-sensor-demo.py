#!/usr/bin/python

import os
import signal
import sys
import time
import RPi.GPIO as GPIO

from FlowerPlatformRuntime.Timer import Timer
from UltrasonicDistanceSensor.UltrasonicDistanceSensor import UltrasonicDistanceSensor


class AppGen :

	distance = None

	def timer1_onTimer(self, event) :
		self.distance = self.ultrasonicDistanceSensor1.distance()
		print("Ping: ")
		print(self.distance)
		print("cm")

	
	def setup(self):
		signal.signal(signal.SIGTERM, self.stop)
		signal.signal(signal.SIGINT, self.stop)
		
		self.timer1 = Timer(True)
		self.timer1.delay = 20
		self.timer1.onTimer = self.timer1_onTimer

		self.ultrasonicDistanceSensor1 = UltrasonicDistanceSensor(23, 24)

		self.timer1.setup()
		self.ultrasonicDistanceSensor1.setup()

	def start(self) :
		self.running = True
		while self.running :
			self.timer1.loop()
			self.ultrasonicDistanceSensor1.loop()
			time.sleep(0.01)
		GPIO.cleanup()
		sys.exit(0)

	def stop(self, signal, frame) :
		self.timer1.stop()
		self.ultrasonicDistanceSensor1.stop()
		self.running = False


if __name__ == '__main__' :
	app = AppGen()
	app.setup()
	app.start()

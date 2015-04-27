#!/usr/bin/python

import time
import MySQLdb
from threading import Thread
import src.lib.system as mysys
import src.lib.debug as debug
import paho.mqtt.client as mqtt

# Device and light pin details #
deviceID = '01'
lightPIN = '12'

#
# The debug function
#
def debug_print(level, s):
	debug.debug_print(level, 'control|rpi: ' + s)

#
# Control rpi's gpio pins based on value in database
#
class GpioControl(Thread):

	def __init__(self, sleep, mqttc):
		''' Constructor. '''
		Thread.__init__(self)
		self.sleep = sleep
		self.db = MySQLdb.connect(host="localhost", user="root", passwd="vignesh2580", db="gpio")
		self.status = 0
		self.mqttc = mqttc

	def run(self):
		while(1):
			cur = self.db.cursor()
			cur.execute("SELECT pinStatus FROM pinStatus WHERE pinNumber='4';")
			status = cur.fetchone()

			if (self.status == int(status[0])):
				debug_print(debug.TRACE, "Light status unchanged " + status[0])
				time.sleep(self.sleep)
				continue

			self.status = int(status[0])
			debug_print(debug.INFO, "Light status changed to " + repr(self.status))
			self.mqttc.publish("control/lights/00",self.status)
			time.sleep(self.sleep)

#
# The main function
#
def main():
	# To limit the size of logfile
	global debugCount
	debugCount = 0

	mqttc = mqtt.Client()
	mqttc.connect("127.0.0.2",1883,60)

	myThreadObj = GpioControl(5, mqttc)
	myThreadObj.start()
	mqttc.loop_forever()
	myThreadObj.join()


if __name__ == "__main__":
	main()

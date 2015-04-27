#!/usr/bin/python

import device_detection_library as ddl
import time
import serial
import MySQLdb
from threading import Thread
import paho.mqtt.client as mqtt
import src.lib.debug as debug

# Device to look for
#device = '50:EA:D6:B6:F5:85'
#device = '192.168.1.201'

#
# The debug function
#
def debug_print(level, s):
	debug.debug_print(level, 'sensing|device_detect: ' + s)

class DeviceDetectionForLight(Thread):

	def __init__(self):
		''' Constructor. '''
		Thread.__init__(self)
		self.db = MySQLdb.connect(host="localhost", user="root",
					passwd="vignesh2580", db="gpio")
		self.mqttc = mqtt.Client()
		self.mqttc.connect("127.0.0.1", 1883, 60)
		self.sleep_time = 5
		self.device = '192.168.1.201'
		self.lastseen  = 0
		#gpio.setwarnings(False)
		#gpio.setmode(gpio.BOARD)
		#gpio.setup(7, gpio.OUT)

	def run(self):

		while(1):

			# Change scanning interval based on time of day #
			hour = int(time.strftime('%H'))
			if (hour >= 17 and hour <= 21):
				if (self.sleep_time != 5):
					self.sleep_time = 5
					debug_print(debug.INFO, 'Setting interval to '
							+ repr(self.sleep_time))
			else:
				if (self.sleep_time != 60):
					self.sleep_time = 60
					debug_print(debug.INFO, 'Setting interval to '
							+ repr(self.sleep_time))

			debug_print(debug.TRACE, 'Scanning Network')
			if(ddl.is_on_network(self.device)):

				# Update lastseen time
				self.mqttc.publish("sensing/devicedetection/live", 1)
				self.lastseen = time.time()
				debug_print(debug.TRACE, 'Device spotted at ' + repr(self.lastseen))

			else:
				self.mqttc.publish("sensing/devicedetection/live", 0)
				debug_print(debug.TRACE, 'Device missing since ' + repr(self.lastseen))

			time.sleep(self.sleep_time)


#############################################################################################
############################# END OF HELPER FUNCTIONS #######################################
#############################################################################################

#
# The main function
#

# To limit the size of logfile
global debugCount
debugCount = 0
#ser_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

myThreadObj = DeviceDetectionForLight()
myThreadObj.start()
myThreadObj.join()

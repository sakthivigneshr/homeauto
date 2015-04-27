#!/usr/bin/python

import time
import MySQLdb
from threading import Thread
import src.lib.system as mysys
import socket
import src.lib.debug as debug

# Device and light pin details #
deviceID = '01'
lightPIN = '12'

def debug_print(level, string):
	debug.debug_print(level, 'control|arduino: ' + string)

class GpioControl(Thread):
	def __init__(self, sleep):
		''' Constructor. '''
		Thread.__init__(self)
		self.sleep = sleep
		self.db = MySQLdb.connect(host="localhost", user="root", passwd="vignesh2580", db="gpio")
		self.status = 0

	def run(self):
		while(1):
			cur = self.db.cursor()
			cur.execute("SELECT pinStatus FROM pinStatus WHERE pinNumber='4';")
			status = cur.fetchone()

			if (self.status == int(status[0])):
				debug_print(debug.TRACE, "Light status unchanged " + status[0])
				time.sleep(self.sleep)
				continue

			debug_print(debug.INFO, "Light status changed to " + status[0])
			self.status = int(status[0])
			cmd = deviceID + status[0] + lightPIN

			conn_success = False
			for i in range(0,3):
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect(('192.168.1.187',5001))
				except socket.error, (value,message): 
					if s: 
						s.close() 
					debug_print(debug.WARN, "Could not open socket: " + message)
					time.sleep(1)
					continue

				conn_success = True
				break

			if (conn_success == False):
				time.sleep(self.sleep)
				continue

			time.sleep(1)
			for i in range(0,3):
				try:
					s.sendall(cmd)
				except socket.error, (value,message):
					debug_print(debug.WARN, "Could not send command: " + message)
					time.sleep(1)
					continue
				break

			time.sleep(1)
			s.close()
			time.sleep(self.sleep - 2)

#
# The main function
#
def main():
	# To limit the size of logfile
	global debugCount
	debugCount = 0

	myThreadObj = GpioControl(5)
	myThreadObj.start()
	myThreadObj.join()

if __name__ == "__main__":
	main()

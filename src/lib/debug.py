#!/usr/bin/python

import time
from src.lib import  system as mysys
import threading

#import RPi.GPIO as gpio
#import serial
#import paho.mqtt.client as mqtt

# Debug levels
ERROR = 1
WARN  = 2
INFO  = 3
TRACE = 4

# Global debug level
debug = TRACE

# Log file name
log_file = '/tmp/homeauto.log'

# Number of lines to store in log file
LOG_SIZE = 10000

# Current log size
debugCount = 0

# Global debug lock
lock = threading.Lock()

#
# The debug function
#
def debug_print(level, text):

	# Do not print if level > global log value #
	if (level > debug):
		return

	with lock:
		global debugCount
		if (debugCount > LOG_SIZE or debugCount == 0):
			debugCount = 1
			mysys.simple_sys_call('echo "' + time.ctime() + '\t: Resetting log file " > ' + log_file)
		mysys.simple_sys_call('echo "' + time.ctime() + '\t: ' + text + '" >> ' + log_file)
		debugCount = debugCount + 1

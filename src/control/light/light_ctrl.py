#!/usr/bin/python

import time
from threading import Thread
import paho.mqtt.client as mqtt
import MySQLdb
import src.lib.system as mysys
import src.lib.debug as debug

# Send mail if person not home for more than 5 hours
THRESHOLD_TIME = 18000

#
# The debug function
#
def debug_print(level, s):
	debug.debug_print(level, 'control|light: ' + s)

#
# Checks for the time to see if this is apt and
# turns the light on
#
def turn_on_lights_if_needed(db):
	# Turn on lights if its above 5pm
	hour = int(time.strftime('%H'))
	month = int(time.strftime('%m'))

	#Daylight saving March to November
	if (month < 3 or month >= 11):
		cutoff = 17
	else:
		cutoff = 19

	if (hour >= cutoff):
		debug_print(debug.INFO, 'Turning on light - welcome back')
		cur = db.cursor()
		cur.execute("UPDATE pinStatus SET pinStatus='1' WHERE " +
				"pinNumber='4';")
		db.commit()
		return 1

	debug_print(debug.TRACE, 'It is not yet time to turn on light')
	return 0

#
# Checks to see if the time is right to turn the lights
# off.
#
def turn_off_lights_if_needed(db):
	# Turn off lights anytime not within 4pm-11:30pm
	hour = int(time.strftime('%H'))
	minute = int(time.strftime('%M'))
	if (hour <= 16 or hour > 23 or (hour == 23 and minute >= 30)):
		debug_print(debug.INFO, 'Turning off light - time ' + repr(hour) +
				' (good night)')
		cur = db.cursor()
		cur.execute("UPDATE pinStatus SET pinStatus='0' WHERE " +
				"pinNumber='4';")
		db.commit()
		return

	debug_print(debug.TRACE, 'It is not yet time to turn off light')

#
# turns the light off
#
def turn_off_lights(db):
	cur = db.cursor()
	cur.execute("UPDATE pinStatus SET pinStatus='0' WHERE " +
			"pinNumber='4';")
	db.commit()

def on_message(mqttc, app_data, msg):

	onNetwork = int(msg.payload)

	# Take details from app data #
	db = app_data.db
	lastseen = app_data.lastseen

	# Compute the diff since lastseen #
	hour = int(time.strftime('%H'))
	diff = time.time() - lastseen

	# check if the lights need to turn off #
	turn_off_lights_if_needed(db)

	if (onNetwork):

		# If this is the first time the device is
		# detected, set last seen
		if (lastseen == 0):
			debug_print(debug.INFO, 'Device spotted for ' 
					+ 'the first time')
			app_data.lastseen = time.time()

		if (diff > THRESHOLD_TIME):
			debug_print(debug.INFO, 'Device spotted after'
			+ ': ' + repr(int(diff)) + ' secs')
			app_data.sakthiIsBack = 1

		if (app_data.sakthiIsBack == 1):
			if (turn_on_lights_if_needed(db)):
				debug_print(debug.INFO, "Lights have been turned on")
				app_data.sakthiIsBack = 0

		# Update lastseen time
		app_data.lastseen = time.time()
		debug_print(debug.TRACE, 'Lastseen time updated ' + repr(app_data.lastseen))

	else:
		if (lastseen == 0):
			debug_print(debug.INFO, 'Device not yet spotted')

		debug_print(debug.TRACE, 'Time since last spotted: ' + repr(int(diff)) + ' secs')

		if (diff > THRESHOLD_TIME):
			debug_print(debug.INFO, "Device missing for greater than threshold time")
			turn_off_lights(db)
			app_data.sakthiIsBack = 0

		debug_print(debug.TRACE, 'Device missing since ' + repr(app_data.lastseen))


def on_subscribe(mqttc, app_data, mid, qos):
	debug_print(debug.INFO, "Subscribe successful")

def on_connect(mqttc, app_data, flags, rc):
	debug_print(debug.INFO, "Connection to mqtt broker successful. Subscribing...")
	mqttc.subscribe("sensing/devicedetection/live")

#############################################################################################
############################# END OF HELPER FUNCTIONS #######################################
#############################################################################################

class myStruct():
	def __init__(self):
		self.db = 0
		self.lastseen = 0
		self.sakthiIsBack = 0
#
# The main function
#
class main():
	app_data = myStruct()
	app_data.db = MySQLdb.connect(host="localhost", user="root",
				passwd="vignesh2580", db="gpio")
	app_data.lastseen = 0
	app_data.sakthiIsBack = 0

	mqttc = mqtt.Client(userdata = app_data)
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_subscribe = on_subscribe

	mqttc.connect("127.0.0.1", 1883, 60)

	# To limit the size of logfile
	global debugCount
	debugCount = 0

	mqttc.loop_forever()

# This prevents main from executing if this is being imported as a module #
if __name__ == "__main__":
	main()

import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime
import src.lib.debug as debug
import paho.mqtt.client as mqtt

stream1 = Stream(
	token='8bwbzgze6l',
	maxpoints=50000,
)

stream2 = Stream(
	token='d2gchv6j41',
	maxpoints=50000,
)

trace1 = Scatter(
    x=[],
    y=[],
    stream=stream1
)

trace2 = Scatter(
    x=[],
    y=[],
    stream=stream2
)

data = Data([trace1, trace2])
py.plot(data)
st1 = py.Stream('8bwbzgze6l')
st2 = py.Stream('d2gchv6j41')

class myStruct():
	def __init__(self):
		self.lum = 0
		self.temp = 0
		self.count = 0

#
# The debug function
#
def debug_print(level, s):
	debug.debug_print(level, 'sensing|temp_bright_plot: ' + s)

def on_message(mqttc, app_data, msg):

	data = msg.payload

	if not data:
		debug_print(debug.WARN, "Received no data...")
		return

	split = data.split()

	if (split[0] != 'light'):
		debug_print(debug.WARN, "Received invalid data: " + data)
		return

	app_data.lum = app_data.lum + int(split[1])
	app_data.temp = app_data.temp + int(split[3])
	count = app_data.count

	debug_print(debug.INFO, "Lum[" + repr(count) + "] = " + split[1] + " Temp[" + repr(count) + "] = " + split[3])
	app_data.count = app_data.count + 1

	if (app_data.count == 6):
		lum = app_data.lum / 6
		temp = app_data.temp / 6
		now = datetime.now().strftime("%H:%M")
		debug_print(debug.INFO, "Lum: " + repr(lum) + " Temp: " + repr(temp) + " " + now)
		st1.write(dict(y=lum, x=now))
		st2.write(dict(y=temp, x=now))
		app_data.lum = 0
		app_data.temp = 0
		app_data.count = 0


def on_subscribe(mqttc, app_data, mid, qos):
	debug_print(debug.INFO, "Subscribe successful")

def on_connect(mqttc, app_data, flags, rc):
	debug_print(debug.INFO, "Connection to mqtt broker successful. Subscribing...")
	mqttc.subscribe("sensing/room1/temp_n_bright")

#
# Plotting class for temperature and brightness
#
class main():


	st1.open()
	st2.open()

	app_data = myStruct()
	mqttc = mqtt.Client(userdata = app_data)
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_subscribe = on_subscribe

	mqttc.connect("127.0.0.1", 1883, 60)

	# To limit the size of logfile
	global debugCount
	debugCount = 0

	mqttc.loop_forever()
	st1.close()
	st2.close()

# This prevents main from executing if this is being imported as a module #
if __name__ == "__main__":
	main()

import time
import socket
from datetime import datetime
import paho.mqtt.client as mqtt

host = ''
port = 5002

def bind_socket(s):
	while 1:
		try:
			s.bind((host,port))
			print 'Bind to port ' + repr(port) + ' success'
			break
		except:
			print 'Failed to open socket, will retry.'
			time.sleep(2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(30)
bind_socket(s)


mqttc = mqtt.Client()
mqttc.connect("127.0.0.2",1883,60)

#
# Start action
#
while 1:
	data = []
	try:
		s.listen(1)
		print 'Listening...'
		conn, addr = s.accept()
		conn.settimeout(30)
		print 'Connection address:', addr
		data = conn.recv(256)
		conn.close()

	except:
		if s:
			s.close()

		if conn:
			conn.close()

		print 'Socket issue in loop, recreating...'
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(30)
		bind_socket(s)
		continue

	if not data:
		print 'Received no data...'
		time.sleep(2)
		continue

	split = data.split()

	if (split[0] != 'light'):
		print "Received invalid data: " + data
		time.sleep(2)
		continue

	mqttc.publish("sensing/room1/temp_n_bright", data)

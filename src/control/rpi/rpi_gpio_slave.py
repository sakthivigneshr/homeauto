import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

OUTPUT_PIN = 18

def on_message(mqttc, app_data, msg):
	level = int(msg.payload)
	print "Received message " + repr(level)
	GPIO.output(OUTPUT_PIN, level)

def on_connect(mqttc, app_data, flags, rc):
	print "Connect successful"
	mqttc.subscribe("control/lights/00")

class main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(OUTPUT_PIN, GPIO.OUT)
	mqttc = mqtt.Client()
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.connect("192.168.1.203", 1883, 60)
	mqttc.loop_forever()

if __name__ == "__main__":
	main()

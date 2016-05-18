import pika
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from threading import Thread

USER = "test"
PASS = "test123"
VHOST = "/cloudlynk"
HOST = "mohawk.link"
KEY = "solfeta"
XCHANGE = "home"
OUTPUT_PIN = 7

def callback(ch, method, properties, body):
	level = int(body)
	print("received msg: " + repr(level))
	GPIO.output(OUTPUT_PIN, level)

def on_message(mqttc, app_data, msg):
        level = int(msg.payload)
        print "Received message " + repr(level)
        GPIO.output(OUTPUT_PIN, level)

def on_connect(mqttc, app_data, flags, rc):
        print "Connect successful"
        mqttc.subscribe("control/lights/00")

class rabbitConnect(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		print "Starting RabbitMQ"
		cred = pika.PlainCredentials(USER, PASS)
		conn = pika.BlockingConnection(pika.ConnectionParameters(
			host=HOST, virtual_host=VHOST, credentials=cred))
		chan = conn.channel()
		chan.exchange_declare(exchange=XCHANGE, type='topic')
		rslt = chan.queue_declare(exclusive=True)
		q = rslt.method.queue
		chan.queue_bind(exchange=XCHANGE, queue=q, routing_key=KEY)
		chan.basic_consume(callback, queue=q, no_ack=True)
		chan.start_consuming()

class mqttConnect(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		print "Starting MQTT"
		mqttc = mqtt.Client()
		mqttc.on_message = on_message
		mqttc.on_connect = on_connect
		mqttc.connect("mohawk.link", 1883, 60)
		mqttc.loop_forever()


class main():

	# Setup the pins
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(OUTPUT_PIN, GPIO.OUT)

	myThreadObj1 = rabbitConnect()
	myThreadObj1.start()

	myThreadObj2 = mqttConnect()
	myThreadObj2.start()

	myThreadObj1.join()
	myThreadObj2.join()

if __name__ == "__main__":
	main()

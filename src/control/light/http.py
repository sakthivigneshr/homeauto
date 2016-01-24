from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import MySQLdb

ADDR = "localhost"
PORT = 8888

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):

	#
	# We can connect outside of the POST call for lower
	# latency and better efficiency. However that involves
	# setting up of 'auto reconnect' on timeouts. So for
	# now I am going with this approach.
	#
	db = MySQLdb.connect(host="localhost", user="root",
			passwd="vignesh2580", db="gpio");

        cmd = self.rfile.read(int(self.headers['Content-Length']))

	if (cmd == 'On'):
		cur = db.cursor()
		cur.execute("UPDATE pinStatus SET pinStatus='1' WHERE " +
				"pinNumber='4';")	
	elif (cmd == 'Off'): 
		cur = db.cursor()
		cur.execute("UPDATE pinStatus SET pinStatus='0' WHERE " +
				"pinNumber='4';")	

	self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write("serverdata")

httpd = HTTPServer(('', PORT), RequestHandler)
httpd.serve_forever()

import os
import subprocess
import shlex
import re
import xml.etree.ElementTree as ET

#global tree
#tree = ET.parse('device_details.xml')

def sys_call(cmd):
	cmd = shlex.split(cmd)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out, err

def simple_sys_call(cmd):
	os.system(cmd)

def get_device_details(device_mac):
	root = tree.getroot();
	for dev in root.findall('device'):
		if (dev.get('mac') == device_mac):
			return dev.find('owner').text + "'s " + dev.find('model').text + " is up"

	return 'Alert! Unknown device on network. MAC address = ' + device_mac

def scan_for_MACs():
	if (sys_call('whoami')[0].strip() != 'root'):
		print "Requires sudo permission!"
		return -1

	result = sys_call('sudo nmap -sP -n 192.168.1.*')[0]
	out = []

	for lines in result.split('\n'):
		if re.search('Nmap scan report for',lines):

			# The lines is of format
			# Nmap scan report for 192.168.1.100
			# Therefore we need the 5th split, which is [3]
			ip_addr = lines.split()[4]

		elif re.search('MAC Address:',lines):

			# This lines is of the format
			# MAC Address: 54:04:A6:8F:9E:CD (Asustek Computer)
			# Therefore we need the 3rd split, which is [2]
			mac_addr = lines.split()[2]

			out.append([ip_addr, mac_addr])

			# Get the name of device
			#device_details = get_device_details(mac_addr)
			#print device_details + ' (' + ip_addr + ')'

	return out

def scan_for_ip(addr):
	result = sys_call('ping -c1 ' + addr)[0]
	if (result.find('100% packet loss') == -1):
		return 1

	return 0

def get_network_details():
	out = scan_for_MACs()
	for i in range(0,len(out)):
		print get_device_details(out[i][1]) + ' (' + out[i][0] + ')'

def is_on_network(addr):

	#
	# If address is not a MAC address, then it must be
	# an ip address. So ping it.
	#
	if (addr.find(':') == -1):
		return scan_for_ip(addr)

	#
	# Else scan for this MAC to be on the network
	#
	out = scan_for_MACs()
	for i in range(0,len(out)):
		if (out[i][1] == mac_addr.upper()):
			return 1

	return 0

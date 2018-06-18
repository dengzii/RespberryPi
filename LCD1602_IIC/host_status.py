import socket
import fcntl
import struct
import psutil
import time
import datetime

BOOT_TIME = psutil.boot_time()

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
		)[20:24])
	except:
		return "None"

def get_up_time():

    up = time.time() - BOOT_TIME
    return datetime.datetime.fromtimestamp(up).strftime('%d-%H%M%S')

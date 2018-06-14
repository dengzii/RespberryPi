#!/usr/bin/env python  
#encoding: utf-8  
from deamon import CDaemon
import LCD1602 as LCD
import host_status as host
import logging
import time
import sys
import os

class PiStatus(CDaemon):

	def __init__(self, name, save_path, stdin=os.devnull, stdout=os.devnull, stderr=os.devnull, home_dir='.', umask=022, verbose=1):  
		CDaemon.__init__(self, save_path, stdin, stdout, stderr, home_dir, umask, verbose)  
		self.name = name
	def run(self, output_fn, **kwargs):  
		fd = open(output_fn, 'w')
		if not LCD.init_lcd():
			fd.write("Failed init lcd1602, stoping now.")
			return
		
		wlan0 = "None"
		eth0 = "None"
		t = 0
		while wlan0 != "None" or eth0 != "None":
			wlan0 = host.get_ip_address("wlan0")
			eth0 = host.get_ip_address("eth0")
			LCD.print_lcd(0, 0, "No network connect")
			LCD.print_lcd(0, 1, "%s times tried" %t)
			t += 0.5
			time.sleep(0.5)
		wlan0 = host.get_ip_address("wlan0")
		LCD.print_lcd(0, 0, "W" + wlan0)
		time.sleep(3)
		rund = 0
		LCD.clear_lcd()
		d = 0
		h = 0
		m = 0
		s = 0
		while True:
			s += 1
			if s%60 == 0:
				s = 0
				m += 1
				if m%60 == 0:
					m=0
					h += 1
					if h%24 == 0:
						h=0
						d += 1
			LCD.print_lcd(0, 0, wlan0)
			LCD.print_lcd(0, 1, "%s %s%s:%s%s:%s%s"%(d, h/10, h%10, m/10, m%10, s/10, s%10))
			time.sleep(1)
		fd.close()  

if __name__ == "__main__":

	p_name = 'pi-status'
	pid_fn = '/tmp/daemon_class.pid'
	log_fn = '/tmp/daemon_class.log' 
	err_fn = '/tmp/daemon_class.err.log' 
	
	ps = PiStatus(p_name, pid_fn, stderr=err_fn, verbose=1) 
	if len(sys.argv) == 1:  
		ps.start(log_fn)
	elif sys.argv[1] == "stop":
		ps.stop();
	elif sys.argv[1] == "restart":
		ps.restart(log_fn)
	elif sys.argv[1] == "status":
		if ps.is_running():
			print "is running ... PID", ps.get_pid()
		else:
			print "is stoped ... ", ps.name
	else:
		print "invalid argument"
	
	
	
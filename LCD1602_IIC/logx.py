import logging

#print on log file
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s <%(levelname)s> [line:%(lineno)d] %(filename)s : %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='trace.log',
                filemode='a')#w a
#print on screem				
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s <%(levelname)s> [line:%(lineno)d] %(filename)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

if __name__ == '__main__':				
	#CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
	logging.critical('This is critical message')
	logging.error('This is error message')
	logging.warning('This is warning message')
	logging.info('This is info message')
	logging.debug('This is debug message')
	#logging.notset('This is notset message')

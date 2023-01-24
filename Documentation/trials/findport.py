import datetime
from datetime import datetime
import serial
from time import time, ctime
import chardet

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
#now = datetime.datetime.now()
#dateTimeObj = datetime.now()
t = time()
ti= ctime(t)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print ( ":" ,data)
	

import datetime
import time
from time import gmtime, strftime

x = datetime.datetime.now()

print(x.strftime("%x"))


while True:
	currenttime = strftime("%H:%M:%S", gmtime())
	print(currenttime)
	# print(x.strftime("%X"))
	time.sleep(1)


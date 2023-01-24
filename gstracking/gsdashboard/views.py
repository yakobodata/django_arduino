from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
from datetime import datetime
import serial
from time import time, ctime
# from gsdashboard import models
from gsdashboard.models import Track


def index(request):
    
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
    #now = datetime.datetime.now()
    #dateTimeObj = datetime.now()
    t = time()
    ti= ctime(t)
    while True:
        data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
        if data:
            print ( ":" ,data)
            Track = data.save()
            Track.save()


            
    return render(request, 'dashboard.html', {})
    #return HttpResponse("Hello, world. You're at the polls index.")
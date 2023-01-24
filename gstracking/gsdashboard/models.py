
from django.db import models
from django.utils.timezone import localtime, now
from datetime import date
import datetime
from time import gmtime, strftime
import time

class Track(models.Model):
    status = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.status

    def save(self,*args,**kwargs):
        #now = datetime.datetime.now().strftime('%H:%M:%S')
        #now = strftime("%H:%M:%S", gmtime())
        while True:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            time.sleep(1)
            self.pub_date = now
        return super().save(*args,**kwargs)  

from django.db import models

# Create your models here.


class Track(models.Model):
	status = models.IntegerField()
	date   = models.DateField()
	time   = models.TimeField()



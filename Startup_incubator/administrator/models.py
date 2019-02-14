from django.db import models
import datetime
from startup.models import Startup

class Documents(models.Model):
	doc = models.FileField(upload_to='documents/')
	typ = models.CharField( max_length= 100 , null=True)
	date = models.DateField(default=datetime.date.today)

class Updates(models.Model):
	info = models.CharField( max_length= 1000 , null=True)
	date = models.DateField(default=datetime.date.today)

class Fund(models.Model):
	typ = models.CharField(max_length=100,null=True)
	startup = models.ForeignKey(Startup,null=True,on_delete=models.CASCADE)
	ppt = models.FileField(upload_to='documents/')
	accept = models.BooleanField(default=False)
	clicked = models.BooleanField(default=False)
	date = models.DateField(default=datetime.date.today)

class Incubation(models.Model):
	startup = models.ForeignKey(Startup,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	accept = models.BooleanField(default=False)
	ppt = models.FileField(upload_to='documents/')
	clicked = models.BooleanField(default=False)
	ddip = models.BooleanField(default=False)
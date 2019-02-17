from django.db import models
import datetime
from startup.models import Startup
from mentor.models import Mentor

class Documents(models.Model):
	doc = models.FileField(upload_to='documents/')
	startup = models.ForeignKey(Startup,null=True,on_delete=models.CASCADE) 
	date = models.DateField(default=datetime.date.today)
	category = models.CharField(max_length= 1000 , null=True, default='document')
	typ = models.CharField(max_length= 1000 , null=True, default='startup')
	video_url = models.CharField(max_length= 1000 , null=True, default='https://www.youtube.com/watch?v=6FlMhxOqiIg')
	mentor_name = models.CharField(max_length= 1000 , null=True, default='Mentor')
	title = models.CharField(max_length= 1000 , null=True, default='some video/doc')

class Updates(models.Model):
	info = models.CharField( max_length= 1000 , null=True)
	schedule = models.DateTimeField(default=datetime.datetime.now())
	title = models.CharField(max_length=1000,null=True)
	date = models.DateTimeField(default=datetime.datetime.now(),blank=True)


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

class AssignMentor(models.Model):
	months = models.CharField(max_length=100,null=True)
	mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE)
	startup = models.ForeignKey(Startup,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
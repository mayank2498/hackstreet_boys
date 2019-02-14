from django.db import models
from investor.models import Investor
from mentor.models import Mentor
from django.contrib.auth.models import User
from login.models import Type

class Founder(models.Model):
	name = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	address = models.CharField( max_length= 100 , null=True)
	def __str__(self):
		return str(self.name)

class Startup(models.Model):
	user = models.ForeignKey(Type,on_delete=models.CASCADE)
	name  = models.CharField( max_length= 100 , null=True)
	founder = models.OneToOneField(Founder,blank=True,null=True)
	investors = models.ManyToManyField(Investor,blank=True)
	mentors = models.ManyToManyField(Mentor,blank=True)
	address = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	description = models.CharField( max_length= 10000 , null=True)
	dipp = models.BooleanField(default=False)
	image = models.FileField(upload_to='profile_photos/')
	dippno = models.CharField(max_length=100,blank=True,null=True)
	#recommended_investors = models.ManyToManyField(Investor,blank=True)
	def __str__(self):
		return str(self.name)

class Connection_investor(models.Model):
	startup = models.ForeignKey(Startup,on_delete=models.CASCADE,null=True)
	investor = models.ForeignKey(Investor,on_delete=models.CASCADE,null=True)
	S_to_I = models.BooleanField(default=True)
	accepted = models.BooleanField(default=False)
	pending = models.BooleanField(default=True)

class Connection_mentor(models.Model):
	startup = models.ForeignKey(Startup,on_delete=models.CASCADE,null=True)
	mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE,null=True)
	S_to_M = models.BooleanField(default=True)
	accepted = models.BooleanField(default=False)
	pending = models.BooleanField(default=True)
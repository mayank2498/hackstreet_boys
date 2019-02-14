from django.db import models
from investor.models import Investor
from mentor.models import Mentor

class Founder(models.Model):
	name = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	address = models.CharField( max_length= 100 , null=True)
	def __str__(self):
		return str(self.name)

class Startup(models.Model):
	name  = models.CharField( max_length= 100 , null=True)
	founders = models.ManyToManyField(Founder,blank=True)
	investors = models.ManyToManyField(Investor,blank=True)
	mentors = models.ManyToManyField(Mentor,blank=True)
	address = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	description = models.CharField( max_length= 10000 , null=True)
	dipp = models.BooleanField(default=False)
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
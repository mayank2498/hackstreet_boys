from django.db import models

import startup
from login.models import Type

class Investor(models.Model):
	
	user = models.ForeignKey(Type,on_delete=models.CASCADE)
	name = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	startups = models.ManyToManyField("startup.Startup",blank=True,null=True)
	description = models.CharField( max_length= 10000 , null=True)
	def __str__(self):
		return str(self.name)



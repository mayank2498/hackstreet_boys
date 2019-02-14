from django.db import models
from login.models import Type
import startup

class Mentor(models.Model):
	user = models.ForeignKey(Type,on_delete=models.CASCADE)
	name = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	startups = models.ManyToManyField("startup.Startup",blank=True,null=True)
	description = models.CharField( max_length= 10000 , null=True)



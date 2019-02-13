from django.db import models

import startup


class Investor(models.Model):
	name = models.CharField( max_length= 100 , null=True)
	email = models.CharField( max_length= 100 , null=True)
	phone_number = models.CharField( max_length= 100 , null=True)
	startups = models.ManyToManyField("startup.Startup",blank=True)
	description = models.CharField( max_length= 10000 , null=True)



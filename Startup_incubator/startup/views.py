from django.shortcuts import render
from django.http import HttpResponse
from investor.models import Investor
from recommendations.train import train_model
from recommendations.test import predict

def index(request):
	return render(request,"startup/register.html")
	return HttpResponse('hello')

<<<<<<< HEAD
=======
def get_recommendations(request):
	startup = "trucks vehicle"
	investors = Investor.objects.all()
	data = []
	for i in investors:
		obj = []
		obj.append(i.name)
		obj.append(i.description)
		data.append(obj)
	predict(data,startup)
	return HttpResponse("done")

def train(request):
	print("Training the model ..... wait.....")
	investors = Investor.objects.all()

	file = open("recommendations/training_data.txt","w")  

	for i in investors:
		file.write(i.description)
		file.write("\n\n\n####\n\n\n")
	file.close()
	print("created training_data.txt file")
	train_model()

	return HttpResponse('trained successfully !')
>>>>>>> 867885ea7fff9d761c8b114e14bb3724aeeb89db

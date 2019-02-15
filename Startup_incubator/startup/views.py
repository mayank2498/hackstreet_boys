from django.shortcuts import render,redirect
from django.http import HttpResponse
from investor.models import Investor
from recommendations.train import train_model
from recommendations.test import predict
from .models import Startup, Incubation_request
from mentor.models import Mentor

def dashboard(request):
	if request.user.is_authenticated() :

		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse("User does not have a startup")

		print('authenticated')
		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse('No startups of this user')

		return render(request,"startup/dashboard.html",{'startup':startup})
	else:
		return redirect('/login')
	


def get_recommendations(request):
	if not request.user.is_authenticated() :
		return redirect('/login')

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



def about_us(request):
	if request.user.is_authenticated() :
		startup = Startup.objects.get(user__user_id=request.user.id)
		print(startup.name)
		return render(request,"startup/about.html",{'startup':startup})
	else:
		return render(request,'front/login.html')
	
def mentors(request):
	if request.user.is_authenticated() :
		mentors = Mentor.objects.all()
		size = len(mentors)
		left = int(size/2)

		mentors_right = mentors[:left]
		mentors_left = mentors[left:]
		startup = Startup.objects.get(user__user_id=request.user.id)
		return render(request,"startup/mentor.html",{'mentors_left':mentors_left,
													'mentors_right':mentors_right,
													'startup':startup})
	else:
		return render(request,'front/login.html')

def mentor_profile_popup(request,pk):
	mentor = Mentor.objects.get(id=pk)
	return render(request,'startup/mentor_profile_popup.html',{'mentor':mentor})

def investors(request):
	if request.user.is_authenticated() :
		investors = Investor.objects.all()
		size = len(investors)
		left = int(size/2)

		investors_right = investors[:left]
		investors_left = investors[left:]
		startup = Startup.objects.get(user__user_id=request.user.id)
		return render(request,"startup/investor.html",{'investors_left':investors_left,
													'investors_right':investors_right,
													'startup':startup})
	else:
		return render(request,'front/login.html')

def investor_profile_popup(request,pk):
	investor = Investor.objects.get(id=pk)
	return render(request,'startup/investor_profile_popup.html',{'investor':investor})


def apply_incubation(request):
	if request.user.is_authenticated() :
		print('authenticated')
	try:
		startup = Startup.objects.get(user__user_id=request.user.id)
	except:
		return HttpResponse('No startups of this user')
	incubation_request = Incubation_request()
	

from django.shortcuts import render,redirect
from django.http import HttpResponse
from investor.models import Investor, Connections
from recommendations.train import train_model
from recommendations.test import predict
from .models import Startup
from administrator.models import Fund,Incubation
from mentor.models import Mentor
from django.views.decorators.csrf import csrf_exempt
import datetime
from login.models import Type
def dashboard(request):
	if request.user.is_authenticated() :

		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse("User does not have a startup")

		msg = ""
		if request.session.get('message', False):
			msg = request.session.get('message')
			del request.session['message']
			print(msg)

		return render(request,"startup/dashboard.html",{'startup':startup,'msg':msg})
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
		print(mentors)
		mentor_data = []
		for m in mentors:
			temp = {}
			temp["mentor_user_id"] = m.user.user.id
			temp["id"] = m.id
			temp["name"] = m.name
			temp["image"] = m.image.url
			temp["description"] = m.description

			obj = Connections.objects.filter(sentfrom_id=request.user.id,sentto_id=m.user.user.id)
			if( len(obj) >= 1 ):
				obj = obj[0]
				if obj.response == False:
					temp["pending"] = 1
			else:
				temp["pending"] = 0
			mentor_data.append(temp)


		print(mentor_data)

		size = len(mentor_data)
		left = int(size/2)

		mentors_right = mentor_data[:left]
		mentors_left = mentor_data[left:]
		startup = Startup.objects.get(user__user_id=request.user.id)
		return render(request,"startup/mentor.html",{'mentors_left':mentors_left,
													'mentors_right':mentors_right,
													'startup':startup})
	else:
		return render(request,'front/login.html')


def startup_profile_popup(request,pk):
	startup = Startup.objects.get(id=pk)
	return render(request,'startup/startup_profile_popup.html',{'startup':startup})

def mentor_profile_popup(request,pk):
	mentor = Mentor.objects.get(id=pk)
	return render(request,'startup/mentor_profile_popup.html',{'mentor':mentor})

def investors(request):
	if request.user.is_authenticated() :

		investors = Investor.objects.all()
		investor_data = []
		for m in investors:
			temp = {}
			temp["investor_user_id"] = m.user.user.id
			temp["id"] = m.id
			temp["name"] = m.name
			temp["image"] = m.image.url
			temp["description"] = m.description

			obj = Connections.objects.filter(sentfrom_id=request.user.id,sentto_id=m.user.user.id)
			if( len(obj) >= 1 ):
				obj = obj[0]
				if obj.response == False:
					temp["pending"] = 1
			else:
				temp["pending"] = 0
			investor_data.append(temp)

		
		size = len(investor_data)
		left = int(size/2)

		investors_right = investor_data[:left]
		investors_left = investor_data[left:]
		startup = Startup.objects.get(user__user_id=request.user.id)
		return render(request,"startup/investor.html",{'investors_left':investors_left,
													'investors_right':investors_right,
													'startup':startup})
	else:
		return render(request,'front/login.html')

def investor_profile_popup(request,pk):
	investor = Investor.objects.get(id=pk)
	return render(request,'startup/investor_profile_popup.html',{'investor':investor})

@csrf_exempt
def apply_incubation(request):
	if request.user.is_authenticated() :
		print('authenticated')

	if request.method == 'GET':
		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse("User does not have a startup")

		return render(request,'startup/apply_incubation.html',{'startup':startup})
	else:
		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse('No startups of this user')

		requests = Incubation.objects.filter(startup__user__user_id=request.user.id)
		fg = 0
		for req in requests:
			if req.clicked == False:
				fg = 1
				break
		if fg == 1:
			request.session['message'] = "You have already applied for Incubation. Wait for reply"
			return redirect('/startup')

		incubation_request = Incubation()
		incubation_request.startup_id = startup.id
		incubation_request.ppt = request.FILES.get('ppt',False)
		incubation_request.save()
		if incubation_request.ppt is False :
			request.session['message'] = "Could not save presentation !" 
		else:
			request.session['message'] = "Applied for Incubation successfully !"
		return redirect('/startup')



@csrf_exempt
def apply_fund(request):
	if request.method == 'GET':
		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse("User does not have a startup")

		return render(request,'startup/apply_fund.html',{'startup':startup})
	else:
		try:
			startup = Startup.objects.get(user__user_id=request.user.id)
		except:
			return HttpResponse('No startups of this user')

		requests = Incubation.objects.filter(startup__user__user_id=request.user.id)
		fg = 0
		for req in requests:
			if req.clicked == False:
				fg = 1
				break
		if fg == 1:
			request.session['message'] = "You have already applied for Fund. Wait for reply"
			return redirect('/startup')

		fund_request = Fund()
		fund_request.startup_id = startup.id
		fund_request.typ = request.POST['type']
		fund_request.ppt = request.FILES.get('ppt',False)
		fund_request.save()
		if fund_request.ppt is False :
			request.session['message'] = "Could not save presentation !" 
		else:
			request.session['message'] = "Applied for Fund successfully !"
		return redirect('/startup')
	


def send_connection_request(request,pk):
	# from will be the logged in user
	fromm = Type.objects.get(user_id=request.user.id)
	# to will be sent from connect button
	to = Type.objects.get(user_id=pk)
	connections = Connections()
	connections.sentfrom_id = fromm.user.id
	connections.sentto_id = pk
	connections.save()
	request.session['message'] = "Sent Connection request "
	return redirect('/startup/')
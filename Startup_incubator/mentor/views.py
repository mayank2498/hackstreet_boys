from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.http import HttpResponse
from investor.models import Investor
from startup.models import Startup 
from django.views.decorators.csrf import csrf_exempt
from .models import Mentor
from login.models import Type
from administrator.models import AssignMentor


def index(request):
	mentor = Mentor.objects.get(user__user_id=request.user.id)
	msg = ""
	if request.session.get('message', False):
		msg = request.session.get('message')
		del request.session['message']
		print(msg)
	return render(request, 'mentor/mentorprofile.html',{'mentor':mentor,'msg':msg})

def show_startups(request):
	try:
		investor = Investor.objects.get(user__user_id=request.user.id)
	except:
		return HttpResponse("wrong input")
	startups = Startup.objects.all()
	size = len(startups)
	left = int(size/2)
	startups_right = startups[:left]
	startups_left = startups[left:]
	return render(request, 'investor/startups.html',{'investor':investor,'startups_left':startups_left,'startups_right':startups_right})

# @csrf_exempt
# def update(request):

# 	investor = Investor.objects.get(user__user_id=request.user.id)
# 	if request.method == "GET":
# 		return render(request, 'investor/investorupdate.html',{'investor':investor})
# 	else:
# 		investor.investment_range = request.POST['investment']
# 		investor.description = request.POST['aboutme']
# 		investor.expertise = request.POST['type']
# 		image = request.FILES.get('image',False)
# 		if image is not False:
# 			startup.image = image
# 		investor.phone_number = request.POST['phoneno']
# 		investor.save()
# 		return redirect('/investor')


# def show_connections(request):
# 	connections1 = Connections.objects.filter(sentfrom_id=request.user.id,accept=True)
# 	print(len(connections1))
# 	connections2 = Connections.objects.filter(sentto_id=request.user.id,accept=True)
# 	print(len(connections1))
# 	startups = []
# 	for connection in connections1:
# 		sentto = connection.sentto
# 		typ = Type.objects.get(user_id=sentto.id)
# 		if typ.typ == "startup":
# 			print("got1")
# 			name = Startup.objects.get(user_id=typ.id)
# 			print(name.description)
# 			startups.append(name)
# 			print(startups)
# 	for connection in connections2:
# 		sentfrom = connection.sentfrom
# 		typ = Type.objects.get(user_id=sentfrom.id)
# 		if typ.typ == "startup":
# 			name = Startup.objects.get(user_id=typ.id)
# 			print("got1")
# 			startups.append(name)
# 	print(startups)
# 	x = []
# 	for s in startups:
# 		obj = {}
# 		obj["name"] = s.name
# 		obj["id"] = s.id
# 		obj["image"] = s.image.url
# 		print(obj["image"])
# 		obj["description"] = s.description
# 		x.append(obj)
# 	left = int(len(x)/2)
# 	startups_left = x[:left]
# 	startups_right = x[left:]
# 	investor = Investor.objects.get(user__user_id=request.user.id)
# 	return render(request, 'investor/myconnections.html',{'investor':investor,'startups_left':startups_left,'startups_right':startups_right})

def assigned_startups(request):
	a = AssignMentor.objects.all()
	for x in a:
		print(x.mentor.name)
	assigns = AssignMentor.objects.filter(mentor__user__user_id=request.user.id)
	if len(assigns) == 0 :
		request.session["message"] = "No startups have been assigned to you"
		return redirect('/mentor')
	print("ok")


	left = int(len(assigns)/2)
	print(left)
	assigns_right = assigns[:left]
	assigns_left = assigns[left:]
	mentor = Mentor.objects.get(user__user_id=request.user.id)
	return render(request,'mentor/assigned_startups.html',{'assigns_left':assigns_left,
														    'assigns_right':assigns_right,
														    'mentor':mentor})

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.http import HttpResponse
from investor.models import Investor
from startup.models import Startup 
from django.views.decorators.csrf import csrf_exempt
from .models import Mentor
from login.models import Type
from administrator.models import AssignMentor,Documents
from administrator.models import Reviews


def index(request):
	mentor = Mentor.objects.get(user__user_id=request.user.id)
	msg = ""
	if request.session.get('message', False):
		msg = request.session.get('message')
		del request.session['message']
		print(msg)
	return render(request, 'mentor/mentorprofile.html',{'mentor':mentor,'msg':msg})

def show_startups(request):
	mentor = Mentor.objects.get(user__user_id=request.user.id)
	try:
		investor = Investor.objects.get(user__user_id=request.user.id)
	except:
		return HttpResponse("wrong input")
	startups = Startup.objects.all()
	size = len(startups)
	left = int(size/2)
	startups_right = startups[:left]
	startups_left = startups[left:]
	return render(request, 'investor/startups.html',{'investor':investor,
													'startups_left':startups_left,
													'startups_right':startups_right,
													'mentor':mentor})


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

@csrf_exempt
def share_videos(request):
	mentor = Mentor.objects.get(user__user_id=request.user.id)
	if request.method == 'GET':
		return render(request,'mentor/share_videos.html',{'mentor':mentor})
	else:
		url = request.POST.get('link')
		name = request.POST.get('name')
		
	
		assigns = AssignMentor.objects.filter(mentor__user__user_id=request.user.id)
		if len(assigns) == 0:
			request.session["message"] = "You cannot upload any videos because you are not assigned to any startup"
			return redirect('/mentor')

		for a in assigns:
			document = Documents()
			document.startup_id = a.startup.id
			document.category = "video"
			document.typ = "mentor"
			document.video_url = url
			document.mentor_name = a.mentor.name
			document.title = name
			document.save()
		request.session['message'] = "Shared the videos to your startups !"
		return redirect('/mentor')
		print("saved !")

@csrf_exempt
def startup_review(request,pk):
	if request.method == "GET":
		startup = Startup.objects.get(id=pk)
		mentor = Mentor.objects.get(user__user_id=request.user.id)
		return render(request,'mentor/startupreview.html',{'startup':startup,'mentor':mentor})
	else:
		review = Reviews()
		review.startup_d = pk
		mentor = Mentor.objects.get(user__user_id=request.user.id)
		review.mentor_id = pk
		review.by_startup = 0
		review.review = request.POST['title']
		review.description = request.POST['desc']
		review.save()
		request.session['message'] = "your review is saved. Thanks for giving the valuable feedaback."
		return redirect('/mentor')


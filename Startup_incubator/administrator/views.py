from django.shortcuts import render
from .models import Incubation,Fund
from django.shortcuts import render
from startup.models import Startup,Founder
from login.models import Type
from investor.models import Investor
from mentor.models import Mentor
from django.contrib.auth.models import User
from investor.models import Investor
from mentor.models import Mentor
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.mail import EmailMessage
#from administrator.models import Documents,Updates


#for admin to add mentor
def add_mentor(request):
	if not request.user.is_authenticated() :
		return redirect('/login')


	if request.method =='GET':
		return render(request,'front/register.html')
	else:
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		user = User()
		user.username = name
		user.set_password(password)
		user.email = email
		user.is_active = True
		user.save()
		typ = Type()
		typ.user_id = user.id
		typ.typ = "mentor"
		typ.save()
		mentor = Mentor()
		mentor.user_id = Type.objects.all(user_id=typ.id)
		mentor.name = name
		mentor.email = email
		mentor.password = password
		mentor.save()
		mail_subject = 'Your account has been activated'
		message = 'Hi ' +  str(name) + 'your account has been activated.Your username is '+ str(email) + ' password is  ' +str(password) 
		to_email = email
		email1 = EmailMessage(mail_subject, message, to=[to_email])
		email1.send()
		return HttpResponse("mentor added")


		
def add_investor(request):

	if not request.user.is_authenticated() :
		return redirect('/login')

	if request.method =='GET':
		return render(request,'front/register.html')
	else:
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		user = User()
		user.username = name
		user.set_password(password)
		user.email = email
		user.is_active = True
		user.save()
		typ = Type()
		typ.user_id = user.id
		typ.typ = "investor"
		typ.save()
		investor = Investor()
		investor.user_id = Type.objects.all(user_id=typ.id)
		investor.name = name
		investor.password = password
		investor.email = email
		investor.save()
		mail_subject = 'Your account has been activated'
		message = 'Hi ' +  str(name) + 'your account has been activated.Your username is '+ str(email) + ' password is  ' +str(password) 
		to_email = email
		email1 = EmailMessage(mail_subject, message, to=[to_email])
		email1.send()
		return HttpResponse("investor added")



#show profiles
def show_startups(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	startups = Startup.objects.all()
	return render(request, 'administrator/showstartups.html',{'startups':startups})
def show_investors(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	investors = Investor.objects.all()
	return render(request, 'administrator/showinvestors.html',{'investors':investors})
def show_mentors(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	mentors = Mentor.objects.all()
	return render(request, 'administrator/showmentors.html',{'mentors':mentors})

def upload_documents(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	doc = request.FILES.get('file',False)
	typ = Type.objects.get(user_id=request.user.id)
	document = Document()
	document.doc = doc
	if typ == "startup":
		document.typ = "startup"
		
	else:
		document.typ = "startup"
	document.save()
	return HttpResponse("document saved")


#posts updates in main page
def update_info(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	info = request.POST['info']
	updates = Updates()
	updates.info = info
	updates.save()
	return HttpResponse("updates added")

def show_incubation(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	incubation = Incubation.objects.filter(clicked=False)
	return render(request, 'administrator/showincubation.html',{'incubation':incubation})


def show_fund(request):
	if not request.user.is_authenticated() :
		return redirect('/login')
	fund = Fund.objects.filter(clicked=False)
	return render(request, 'administrator/showfund.html',{'fund':fund})
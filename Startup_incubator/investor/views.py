from django.shortcuts import render,redirect
from django.http import HttpResponse
from investor.models import Investor
from startup.models import Startup 
from django.views.decorators.csrf import csrf_exempt
from .models import Connections
from login.models import Type

def index(request):
	investor = Investor.objects.get(user__user_id=request.user.id)
	return render(request, 'investor/investorprofile.html',{'investor':investor})

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

@csrf_exempt
def update(request):

	investor = Investor.objects.get(user__user_id=request.user.id)
	if request.method == "GET":
		return render(request, 'investor/investorupdate.html',{'investor':investor})
	else:
		investor.investment_range = request.POST['investment']
		investor.description = request.POST['aboutme']
		investor.expertise = request.POST['type']
		image = request.FILES.get('image',False)
		if image is not False:
			startup.image = image
		investor.phone_number = request.POST['phoneno']
		investor.save()
		return redirect('/investor')

def show_connections(request):
	connections = Connections.objects.filter(sentfrom_id=request.user.id)
	connection = connections[0]
	sentto = connection.sentto
	
	typ = Type.objects.get(user_id=sentto.id)
	if typ.typ == "investor":
		name = Investor.objects.get(user_id=typ.id)
		name = name.description

	return HttpResponse(str(sentto)+ ' '+str(typ.typ))


		
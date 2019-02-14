from django.shortcuts import render
from startup.models import Startup
from .models import Type
from investor.models import Investor
from mentor.models import Mentor
from django.contrib.auth.models import User
from investor.models import Investor
from mentor.models import Mentor
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(request):
	if request.method =='GET':
		return render(request,'startup/register.html')
	else:
		name = request.POST['name']
		founder_name = request.POST['founder_name']
		founder_email = request.POST['founder_name']
		founder_phone = request.POST['founder_name']
		founder_address = request.POST['founder_name']
		dipp = request.POST['dipp']
		address = request.POST['last_name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		password = request.POST['password']

		founder = Founder()
		founder.name = founder_name
		founder.email = founder_email
		founder.phone_number = founder_phone
		founder.address = founder_address
		founder.save()
		image = request.FILES.get('image',False)
		user = User()
		user.username = name
		user.set_password(password)
		user.email = email
		user.is_active = True
		user.save()
		cat = Type()
		user1 = User.objects.get(username=name)
		cat.user_id  = user1.user_id
		cat.save()
		startup = Startup()
		user1 = Type.objects.get(id=cat.id)
		startup.user_id = user1.id
		startup.name = name
		startup.address = address
		startup.email = email
		startup.dipp = dipp
		f1 = Founder.objects.get(id=founder.id)
		startup.founders_id = f1.id
		startup.description = description
		startup.phone_number = mobile
		startup.image = image
		startup.save()
		return redirect("startup/")

def index(request):
	pass



def login_user(request):
	if request.method =='GET':
		return render(request,'user_panel/register.html')
	else:
		email = request.POST['email']
		password = request.POST['password']
		cat = request.POST['type']
		
		user = User.objects.get(email=email)
		user = authenticate(username=user1.username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				user1 = Type.objects.get(user_id=user.id)
				if user1.type == "startup":
					startup = Startup.objects.get(user_id=user1.id)

				if user1.type == "investor":
					startup = Investor.objects.get(user_id=user1.id)
				if user1.type == "mentor":
					startup = Mentor.objects.get(user_id=user1.id)
				pass
			else:
				return HttpResponse("tsdasd");













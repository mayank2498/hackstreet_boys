from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Rent
def get_admin(id):
 	admin = User.objects.get(id=id)
 	return admin

def index(request):
	rents = Rent.objects.filter(curr=True)
	data_upper = [{'1':0},{'2':0}]
	data_lower = [{'3':0},{'4':0}]
	for r in rents:
		for d in data_upper:
			key = list(d.keys())[0]
			print(key)
			if key==r.room_no :
				d[r.room_no] = 1
				d["startup"] = r.startup.name
				d["duration"] = r.duration
				d["image"] = r.startup.image.url
				d["date_alloted"] = r.date_alloted
		for d in data_lower:
			key = list(d.keys())[0]
			print(key)
			if key==r.room_no :
				d[r.room_no] = 1
				d["startup"] = r.startup.name

	print(data_upper)
	return render(request,'rent/rentmap.html',{	'data_upper':data_upper,
												'data_lower':data_lower,
												'admin':get_admin(request.user.id)
												})



def give_rent(request):
	return render(request,'rent/rentmap.html',{'admin':get_admin(request.user.id)})
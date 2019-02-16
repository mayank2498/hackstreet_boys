from django.contrib import admin

from .models import Founder, Startup,Tickets

admin.site.register(Founder)
admin.site.register(Tickets)

# Register your models here.

class StartupAdmin(admin.ModelAdmin):
	list_display = ["name"]
admin.site.register(Startup,StartupAdmin)

class Incubation_requestAdmin(admin.ModelAdmin):
	list_display = ["ppt","date_applied","accepted","pending"]

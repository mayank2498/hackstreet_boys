from django.contrib import admin

from .models import Founder, Startup

admin.site.register(Founder)
#admin.site.register(Startup)


# Register your models here.

class StartupAdmin(admin.ModelAdmin):
	list_display = ["name"]
admin.site.register(Startup,StartupAdmin)
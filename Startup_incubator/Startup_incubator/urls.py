
from django.conf.urls import url,include
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^startup/',include('startup.urls',namespace='startup')),
    url(r'^investor/',include('investor.urls',namespace='investor')),
    url(r'^mentor/',include('mentor.urls',namespace='mentor')),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'^register/',views.register, name='register'),
]

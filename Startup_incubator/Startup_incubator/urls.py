
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^startup/',include('startup.urls',namespace='startup')),
    url(r'^investor/',include('investor.urls',namespace='investor')),
    url(r'^mentor/',include('mentor.urls',namespace='mentor')),
]

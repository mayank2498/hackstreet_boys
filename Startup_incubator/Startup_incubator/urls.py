
from django.conf.urls import url,include
from django.contrib import admin
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^startup/',include('startup.urls',namespace='startup')),
    url(r'^investor/',include('investor.urls',namespace='investor')),
    url(r'^mentor/',include('mentor.urls',namespace='mentor')),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'^register/',views.register, name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
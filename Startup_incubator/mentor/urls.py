from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^assigned_startups$', views.assigned_startups, name='assigned_startups'),
       
]
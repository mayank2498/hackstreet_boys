from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^assigned_startups$', views.assigned_startups, name='assigned_startups'),
    url(r'^share_videos$', views.share_videos, name='share_videos')
]


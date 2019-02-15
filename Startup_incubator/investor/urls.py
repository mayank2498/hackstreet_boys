from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_startups$', views.show_startups, name='show_startups'),
    url(r'^update$', views.update, name='show_startups'),
    url(r'^show_connections$', views.show_connections, name='show_connections'),

]
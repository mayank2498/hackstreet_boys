from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    


=======
    url(r'^train/$',views.train, name='train'),
    url(r'^predict/$',views.get_recommendations, name='predict'),
    
>>>>>>> 867885ea7fff9d761c8b114e14bb3724aeeb89db
]
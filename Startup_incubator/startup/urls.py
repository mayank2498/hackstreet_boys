from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^train/$',views.train, name='train'),
    url(r'^predict/$',views.get_recommendations, name='predict'),
]
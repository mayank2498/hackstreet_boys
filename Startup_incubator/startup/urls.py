from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^train/$',views.train, name='train'),
    url(r'^predict/$',views.get_recommendations, name='predict'),
    url(r'^about/$',views.about_us),
    url(r'^mentors/$',views.mentors),
    url(r'^investors/$',views.investors),
    url(r'^mentor_popup/(?P<pk>[0-9]+)$',views.mentor_profile_popup,name='mentor_popup'),
    url(r'^investor_popup/(?P<pk>[0-9]+)$',views.investor_profile_popup,name='investor_popup'),
    url(r'^startup_popup/(?P<pk>[0-9]+)$',views.startup_profile_popup,name='startup_popup'),
    url(r'^apply_incubation/$',views.apply_incubation),

]
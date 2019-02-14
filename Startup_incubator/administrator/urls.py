from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_mentor$', views.add_mentor, name='add_mentor'),
    url(r'^add_investor$', views.add_investor, name='add_investor'),
    url(r'^show_startups$', views.show_startups, name='show_startups'),
    url(r'^show_investors$', views.show_investors, name='show_investors'),
    url(r'^show_mentors$', views.show_mentors, name='show_mentors'),
    url(r'^upload_documents$', views.upload_documents, name='upload_documents'),
    url(r'^update_info$', views.update_info, name='update_info'),


]
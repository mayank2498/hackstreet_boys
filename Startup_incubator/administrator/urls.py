from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_mentor$', views.add_mentor, name='add_mentor'),
    url(r'^add_investor$', views.add_investor, name='add_investor'),

    url(r'^show_startups$', views.show_startups, name='show_startups'),
    url(r'^show_investors$', views.show_investors, name='show_investors'),
    url(r'^show_mentors$', views.show_mentors, name='show_mentors'),
    #url(r'^test$', views.test),
    url(r'^upload_documents$', views.upload_documents, name='upload_documents'),
    url(r'^update_info$', views.update_info, name='update_info'),
    url(r'^show_tickets$', views.show_tickets, name='show_tickets'),
    url(r'^show_incubation$', views.show_incubation, name='show_incunbation'),
    url(r'^accept_fund/(?P<pk>[0-9]+)$',views.accept_fund,name='accept_fund'),
    url(r'^reject_fund/(?P<pk>[0-9]+)$',views.reject_fund,name='reject_fund'),
    url(r'^accept_incubation/(?P<pk>[0-9]+)$',views.accept_incubation,name='accept_incubation'),
    url(r'^reject_incubation/(?P<pk>[0-9]+)$',views.reject_incubation,name='reject_incubation'),
    url(r'^show_ticket/(?P<pk>[0-9]+)$',views.show_ticket,name='show_ticket'),
    url(r'^solve_ticket/(?P<pk>[0-9]+)$',views.solve_ticket,name='solve_ticket')
]
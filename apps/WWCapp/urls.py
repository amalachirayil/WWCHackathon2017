from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^donor', views.donations),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^viewdonations', views.viewdonations),
    url(r'^requestitems', views.requestitems),
    url(r'^requestsubmit', views.requestsubmit)
]

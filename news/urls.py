from django.conf.urls import url
from . import views

urlpattern = [
    url('^$', views.welcome, name = 'welcome')
]
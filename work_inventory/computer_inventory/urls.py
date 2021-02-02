from django.conf.urls import url
from .views import *
urlpatterns =[
    url(r'^$', index, name ='index'),
    url(r'^computers$', display_computers, name= "display_computers"),

    url(r"add_computer", add_computer, name="add_computer")
]

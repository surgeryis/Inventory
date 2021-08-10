from django.conf.urls import url
from django.urls import path
from .views import *
urlpatterns =[
    url(r'^$', display_computers, name ='display_computers'),
    url(r'^computers$', display_computers, name= "display_computers"),

    url(r"add_computer", add_computer, name="add_computer"),
    path('search/', SearchResults.as_view(),name = 'Search Results'),
    url('r^index', index, name ='index')

]

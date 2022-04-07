from re import I
from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [ 
    path('premium/',views.Premium,name="premium")
]
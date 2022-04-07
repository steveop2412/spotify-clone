from re import I
from django.urls import path
from .import views

urlpatterns= [
    path('sign-up/',views.Signup,name="signup"),
    path('sign-mob/',views.SignMob,name="signmob"),
]
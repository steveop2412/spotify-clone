from django.urls import path
from .import views

urlpatterns = [
    path('support/',views.Support,name="support"),
]
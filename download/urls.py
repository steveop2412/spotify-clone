from django.urls import path
from .import views

urlpatterns = [
    path('download/',views.Download,name="download"),
]
from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def Premium(request):
    return render(request,'premium.html')
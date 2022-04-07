from django.shortcuts import render

# Create your views here.
def Download(request):
    return render(request,'download.html')
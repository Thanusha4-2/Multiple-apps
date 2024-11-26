from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def B_Tech(request):
    return HttpResponse('<h1>B.Tech at CSE Stream at KSRM College of Engineering</h1>')

def CGPA(request):
    return HttpResponse('<h1>I have 8.7 Throughout my Bachelores</h1>')

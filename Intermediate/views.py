from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Junior_college(request):
    return HttpResponse('<h1>Intermediate In Sri Chaitanya Junior College</h1>')

def Course(request):
    return HttpResponse('<h1>I completed my Intermediate in MPC</h1>')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def First(request):
    return HttpResponse('<h1>Schooling from 1st to 10th in S.F.S E.M High School</h1>')

def GPA(request):
    return HttpResponse('<h1>I got 10 GPA in 10th</h1>')

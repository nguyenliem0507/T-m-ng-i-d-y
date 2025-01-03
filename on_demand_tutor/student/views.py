from django.shortcuts import render
from django.http import HttpResponse

def Student(request):
    return HttpResponse("Hello world!")
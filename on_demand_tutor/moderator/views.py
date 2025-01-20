# moderator/views.py

from django.shortcuts import render
from django.http import HttpResponse

def Moderator(request):
    return HttpResponse("Hello moderator!")


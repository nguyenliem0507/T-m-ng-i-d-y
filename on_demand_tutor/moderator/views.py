# moderator/views.py

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.shortcuts import redirect


def Moderator(request):
    return HttpResponse("Hello moderator!")

def moderator_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/moderator-login/')  


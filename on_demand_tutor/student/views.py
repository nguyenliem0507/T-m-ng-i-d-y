from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.shortcuts import redirect

def Student(request):
    return HttpResponse("Hello world!")

def user_logout(request):
    logout(request)
    return redirect('/')  # Chuyển hướng về trang chủ hoặc trang đăng nhập
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Tutor

def Tutor(request):
    return HttpResponse("Hello world!")

def tutor_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/tutor-login/')  # Chuyển hướng về trang đăng nhập của tutor

def tutor_index(request):
    tutors = Tutor.objects.all()  # Lấy danh sách tutor
    return render(request, 'tutor-index.html', {'tutor': tutors})

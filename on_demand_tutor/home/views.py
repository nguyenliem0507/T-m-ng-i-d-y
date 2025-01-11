from urllib import request
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from tutor.models import Tutor
from student.models import Student
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.

def home (request):
    return render(request, 'home/index.html')

def tutor(request):
    tutor = Tutor.objects.all()
    template = loader.get_template('tutor/tutor-index.html')
    context = {
        'tutor': tutor
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Nhận username từ form
        password = request.POST['password']  # Nhận password từ form

        # Kiểm tra thông tin đăng nhập
        try:
            # Tìm user trong bảng Student
            student = Student.objects.get(Username=username)

            # Kiểm tra mật khẩu
            if student.Password == password:  
                return redirect('/tutor-index')  
            else:
                return HttpResponse("Invalid credentials. Please check your username or password.")
        except Student.DoesNotExist:
            return HttpResponse("Invalid credentials. Please check your username or password.")

    return render(request, 'student/student-login.html')

def register_view(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        fullname = request.POST['fullname']
        birthdate = request.POST['birthdate']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']

        # Kiểm tra mật khẩu
        if password != confirm_password:
            return HttpResponse("Passwords do not match!")

        # Kiểm tra email hợp lệ
        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse("Invalid email address!")

        # Kiểm tra số điện thoại
        phone_validator = RegexValidator(
            regex=r'^\d{10}$',
            message='Phone number must be 10 digits',
        )
        try:
            phone_validator(phone)
        except ValidationError:
            return HttpResponse("Invalid phone number!")

        # Kiểm tra username/email đã tồn tại
        if Student.objects.filter(Username=username).exists():
            return HttpResponse("Username already registered!")
        if Student.objects.filter(Email=email).exists():
            return HttpResponse("Email already registered!")


        # Tạo tài khoản mới
        student = Student(
            Username=username,
            Password=password,  
            FullName=fullname,
            BirthDate=birthdate,
            Gender=gender,
            Phone=phone,
            Email=email,
        )
        student.save()

        return redirect('/student-login') 

    return render(request, 'student/student-register.html')

def tutor_login(request):
    if request.method == 'POST':
        username = request.POST['username']  # Nhận username từ form
        password = request.POST['password']  # Nhận password từ form

        # Kiểm tra thông tin đăng nhập
        try:
            # Tìm user trong bảng Student
            tutor = Tutor.objects.get(Username=username)

            # Kiểm tra mật khẩu
            if tutor.Password == password:  
                return redirect('/tutor-index')  
            else:
                return HttpResponse("Invalid credentials. Please check your username or password.")
        except Student.DoesNotExist:
            return HttpResponse("Invalid credentials. Please check your username or password.")
    return render(request, 'tutor/tutor-login.html')

    if request.method == 'POST':
        email = request.POST.get('email', tutor.Email)
        phone = request.POST.get('phone', tutor.Phone)
        degree = request.POST.get('degree', tutor.Degree)
        password = request.POST.get('password', tutor.Password)

        tutor.Email = email
        tutor.Phone = phone
        tutor.Degree = degree
        tutor.Password = password
        tutor.save()

        return redirect('/tutor-edited')

    return render(request, 'tutor/tutor-edited.html', {'tutor': tutor})
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from tutor.models import Tutor
from student.models import Student
from django.shortcuts import get_object_or_404

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
        username = request.POST['username']
        password = request.POST['password']  

        try:
            student = Student.objects.get(Username=username)
            if student.Password == password:  
                request.session['username'] = username
                return redirect('/tutor-index')  
            else:
                return HttpResponse("Invalid credentials. Please check your username or password.")
        except Student.DoesNotExist:
            return HttpResponse("Invalid credentials. Please check your username or password.")

    return render(request, 'student/student-login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        fullname = request.POST['fullname']
        birthdate = request.POST['birthdate']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']

        if password != confirm_password:
            return HttpResponse("Passwords do not match!")

        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse("Invalid email address!")

        phone_validator = RegexValidator(
            regex=r'^\d{10}$',
            message='Phone number must be 10 digits',
        )
        try:
            phone_validator(phone)
        except ValidationError:
            return HttpResponse("Invalid phone number!")

        if Student.objects.filter(Username=username).exists():
            return HttpResponse("Username already registered!")
        if Student.objects.filter(Email=email).exists():
            return HttpResponse("Email already registered!")

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
        username = request.POST['username']
        password = request.POST['password']

        try:
            tutor = Tutor.objects.get(Username=username)

            if tutor.Password == password:
                request.session['username'] = username
                return redirect('/tutor-edited')
            else:
                return HttpResponse("Invalid credentials. Please check your username or password.")
        except Tutor.DoesNotExist:
            return HttpResponse("Invalid credentials. Please check your username or password.")

    return render(request, 'tutor/tutor-login.html')

def tutor_edited(request):
    username = request.session.get('username')
    if not username:
        return redirect('/tutor-login')

    tutor = get_object_or_404(Tutor, Username=username)

    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        password = request.POST.get('password')

        if email:
            tutor.Email = email
        if phone:
            tutor.Phone = phone
        if degree:
            tutor.Degree = degree
        if password:
            tutor.Password = password

        tutor.save()
        return redirect('/tutor-edited')

    return render(request, 'tutor/tutor-edited.html', {'tutor': tutor})

def student_edited(request):
    username = request.session.get('username')
    student = get_object_or_404(Student, Username=username)

    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if email:
            student.Email = email
        if phone:
            student.Phone = phone
        if password:
            student.Password = password

        student.save()
        return redirect('/student-edited')

    return render(request, 'student/student-edited.html', {'student': student})


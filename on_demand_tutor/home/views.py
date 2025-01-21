from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from tutor.models import Tutor
from student.models import Student
from booking.models import Booking
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from moderator.models import Moderator
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def tutor(request):
    search_query = request.GET.get('search', '')

    if search_query:
        tutor = Tutor.objects.filter(FullName__icontains=search_query)
    else:
        tutor = Tutor.objects.all()

    template = loader.get_template('tutor/tutor-index.html')
    context = {
        'tutor': tutor,
        'search_query': search_query,
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
    if not username:
        return redirect('/student-login')

    try:
        student = Student.objects.get(Username=username)
    except Student.DoesNotExist:
        return HttpResponse("Student not found.")

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
        messages.success(request, "Your profile has been updated successfully.")
        return redirect('/student-edited')

    return render(request, 'student/student-edited.html', {'student': student})

def student_book(request, tutor_username):
    username = request.session.get('username')
    
    if not username:
        return redirect('/student-login')

    # Lấy tutor theo username
    tutor = get_object_or_404(Tutor, Username=tutor_username)
    student = get_object_or_404(Student, Username=username)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Kiểm tra nếu lịch đã trùng
        if Booking.objects.filter(
            tutor=tutor, start_date__lte=end_date, end_date__gte=start_date
        ).exists():
            return HttpResponse("This tutor is already booked for the selected time.")

        # Tạo booking mới
        booking = Booking(
            student=student,
            tutor=tutor,
            start_date=start_date,
            end_date=end_date
        )
        booking.save()

        return redirect('/tutor-index')

    return render(request, 'student/student-book.html', {'tutor': tutor})

def student_schedule(request):
    username = request.session.get('username')
    if not username:
        return redirect('/student-login')

    student = get_object_or_404(Student, Username=username)  

    bookings = Booking.objects.filter(student=student).select_related('tutor')

    return render(request, 'student/student-schedule.html', {'bookings': bookings})

@csrf_exempt
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('student-schedule')

def leave_feedback(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        if feedback:
            booking.feedback = feedback
            booking.save()
            messages.success(request, "Feedback submitted successfully.")
        else:
            messages.error(request, "Feedback cannot be empty.")

    return redirect('student-schedule')

def moderator_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            moderator = Moderator.objects.get(Username=username)

            if moderator.Password == password:
                request.session['username'] = username
                return redirect('/moderator-feedback')  # Thay đổi URL tới dashboard của Moderator
            else:
                return HttpResponse("Invalid credentials. Please check your username or password.")
        except Moderator.DoesNotExist:
            return HttpResponse("Invalid credentials. Please check your username or password.")

    return render(request, 'moderator/moderator-login.html')  # Chuyển đến template login của moderator

def moderator_feedback(request):
    # Kiểm tra session của moderator
    username = request.session.get('username')
    if not username:
        return redirect('/moderator-login')

    # Lấy danh sách feedback chưa được duyệt
    feedbacks = Booking.objects.filter(feedback__isnull=False, approved=False).select_related('student', 'tutor')

    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'moderator/moderator-feedback.html', context)

def approve_feedback(request, id):
    booking = get_object_or_404(Booking, id=id)
    
    # Phê duyệt feedback
    booking.approved = True
    booking.save()
    
    # Quay lại trang moderator feedback
    return redirect('moderator_feedback')

@login_required(login_url='/tutor-login/')
def view_approved_feedback(request):
    username = request.session.get('username')
    if not username:
        return redirect('/tutor-login/')

    # Lấy thông tin tutor dựa trên session
    tutor = get_object_or_404(Tutor, Username=username)

    # Lấy tất cả feedback đã được duyệt của Tutor này
    approved_feedbacks = Booking.objects.filter(
        tutor=tutor,
        feedback__isnull=False,
        approved=True  # Chỉ lấy feedback đã được duyệt
    )

    context = {
        'approved_feedbacks': approved_feedbacks
    }
    return render(request, 'tutor/view-feedback.html', context)

from django.shortcuts import render
from django.http import HttpResponse

def Tutor(request):
    return HttpResponse("Hello world!")
from django.shortcuts import render
from .models import Feedback

def schedule(request):
    feedbacks = Feedback.objects.filter(tutor=request.user, is_approved=True)  # Chỉ phản hồi đã được duyệt
    return render(request, 'tutor/schedule.html', {'feedbacks': feedbacks})

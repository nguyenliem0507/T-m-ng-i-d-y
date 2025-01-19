# moderator/views.py

from django.shortcuts import render
from django.http import HttpResponse

def Moderator(request):
    return HttpResponse("Hello moderator!")
from django.shortcuts import render, get_object_or_404, redirect
from tutor.models import Feedback

def approve_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.is_approved = True
    feedback.save()
    return redirect('feedback_list')  # Điều hướng về trang danh sách phản hồi

def feedback_list(request):
    feedbacks = Feedback.objects.filter(is_approved=False)  # Lọc các phản hồi chưa được phê duyệt
    return render(request, 'moderator/feedback_list.html', {'feedbacks': feedbacks})


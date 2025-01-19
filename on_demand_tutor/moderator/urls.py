from django.urls import path
from . import views

urlpatterns = [
    path('moderator/', views.Moderator, name='moderator'),
]

urlpatterns = [
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/approve/<int:feedback_id>/', views.approve_feedback, name='approve_feedback'),
]

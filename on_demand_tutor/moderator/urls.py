from django.urls import path
from . import views

urlpatterns = [
    path('moderator/', views.Moderator, name='moderator'),
]



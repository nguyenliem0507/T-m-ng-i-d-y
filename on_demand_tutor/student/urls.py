from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.Student, name='student'),
]
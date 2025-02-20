from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.Student, name='student'),
    path('logout/', views.user_logout, name='logout'),
]
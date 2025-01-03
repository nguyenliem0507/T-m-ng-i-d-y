from django.contrib import admin
from django.urls import path, include
from tutor import views  # Import views của bạn
from .import view
urlpatterns = [
    path('', views.home, name= "home")
]
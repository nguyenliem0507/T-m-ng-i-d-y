from django.urls import path
from . import views

urlpatterns = [
    path('tutor/', views.Tutor, name='tutor'),
]
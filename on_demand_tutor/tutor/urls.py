from django.urls import path
from . import views

urlpatterns = [
    path('tutor/', views.Tutor, name='tutor'),
    path('logout/', views.tutor_logout, name='tutor-logout'),
]

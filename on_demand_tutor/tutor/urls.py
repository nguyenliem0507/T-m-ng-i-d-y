from django.urls import path
from . import views

urlpatterns = [
    path('tutor/', views.Tutor, name='tutor'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule, name='tutor_schedule'),
]

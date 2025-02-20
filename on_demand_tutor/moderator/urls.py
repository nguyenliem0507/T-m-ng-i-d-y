from django.urls import path
from . import views

urlpatterns = [
    path('moderator/', views.Moderator, name='moderator'),
    path('logout/', views.moderator_logout, name='moderator-logout'),

]


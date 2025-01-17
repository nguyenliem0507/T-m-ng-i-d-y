from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('tutor-index', views.tutor, name='tutor'),
    path('student-login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('tutor-login/', views.tutor_login, name='tutor-login'),
    path('tutor-edited/', views.tutor_edited, name='tutor-edited'),
    path('student-edited/', views.student_edited, name='student-edited'),
    path('student-book/<str:tutor_username>/', views.student_book, name='student-book'),
]
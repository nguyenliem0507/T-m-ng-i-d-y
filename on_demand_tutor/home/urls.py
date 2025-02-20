from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tutor-index', views.tutor, name='tutor'),
    path('student-login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('tutor-login/', views.tutor_login, name='tutor-login'),
    path('tutor-edited/', views.tutor_edited, name='tutor-edited'),
    path('student-edited/', views.student_edited, name='student-edited'),
    path('student-book/<str:tutor_username>/', views.student_book, name='student-book'),
    path('student-schedule/', views.student_schedule, name='student-schedule'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete-booking'),
    path('leave-feedback/<int:booking_id>/', views.leave_feedback, name='leave-feedback'),
    path('moderator-login/', views.moderator_login, name='moderator-login'),
    path('moderator-feedback/', views.moderator_feedback, name='moderator_feedback'),
    path('approve-feedback/<int:id>/', views.approve_feedback, name='approve_feedback'),
    path('tutor-feedback/', views.view_approved_feedback, name='tutor-feedback'),
    path('wallet/', views.wallet_view, name='wallet-view'),
    path('wallet/add-funds/', views.add_funds, name='add-funds'),
    path('wallet/view-balance/', views.view_balance, name='view-balance'),
]


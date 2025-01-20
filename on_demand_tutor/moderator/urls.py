from django.urls import path
from .views import ModeratorLoginView, ModeratorRegisterView

urlpatterns = [
    path('login/', ModeratorLoginView.as_view(), name='moderator_login'),
    path('register/', ModeratorRegisterView.as_view(), name='moderator_register'),
]

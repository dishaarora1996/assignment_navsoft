from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]

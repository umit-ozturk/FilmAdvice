from django.urls import path
from filmAdvice.profile.views import LoginView, LogoutView, RegisterView, ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="auth/login.html"), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('register/', RegisterView.as_view(template_name="auth/register.html"), name='auth_registration'),
    path('user/<str:username>/', ProfileDetailView.as_view(template_name="auth/profile.html"), name='auth_profile'),
]
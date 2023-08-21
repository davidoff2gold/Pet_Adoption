from django.urls import path
from .views import HomeView, RegisterView, AboutView, DonateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("donate", DonateView.as_view(), name="donate"),


    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]
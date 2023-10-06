from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),
]
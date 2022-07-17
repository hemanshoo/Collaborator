from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login-login'),
    path('signup',views.signup,name='login-signup'),
    path('',views.home,name='login-home'),
    path('logout',views.logout,name='login-logout')
]
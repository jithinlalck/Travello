from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.fn_register, name='register'),
    path('login', views.fn_Login, name='login'),
    path('logout',views.fn_Logout, name='logout'),


]


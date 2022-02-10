from django.urls import path
from . import views
urlpatterns = [
    path('',views.fnIndex,name='index'),
    path('services/',views.fnServices, name='services'),
    path('news/', views.fnNews, name='news'),
    path('contact/', views.fnContact, name='contact'),
    path('home/',views.fn_home,name='home'),
    path('about/',views.fn_about,name='about'),
]
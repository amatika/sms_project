from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('home/', views.home, name='myhome'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.login, name='myloginpage'),
]
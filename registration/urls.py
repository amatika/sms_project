from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('', views.home, name='myhome'),
    path('courses/', views.courses, name='courses'),
    path('coursesdash/', views.coursedashboard, name='coursesdashboard'),
    path('login/', views.login, name='myloginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adduser',views.adduser, name='addinguser'),

    path('addstudent',views.addstudent, name='addingstudent'),


    path('editstudent/<id>',views.editstudent, name='editstudent'),
    path('updatestudent/<id>',views.updatestudent, name='updatestudent'),
    path('deletestudent/<id>',views.deletestudent)
]
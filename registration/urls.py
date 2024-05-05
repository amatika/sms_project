from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('', views.home, name='myhome'),
    path('courses/', views.courses, name='courses'),
    path('coursesdash/', views.coursedashboard, name='coursesdashboard'),
    path('thelogin/', views.login, name='myloginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adduser',views.adduser, name='addinguser'),
    path('mytestform',views.gettestform, name='testform'),
    path('addstudent',views.addstudent, name='addingstudent'),

    path('editstudent/<id>',views.editstudent, name='editstudent'),


    path('updatestudent/<id>',views.updatestudent, name='updatestudent'),


    path('deletestudent/<id>',views.deletestudent), #the url comes with the id as a parameter
    path('create/', views.create_course, name='create_course'),
    path('success/', views.success, name='success'),
    path('update/<int:pk>/', views.update_course, name='update_course'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
    path('loginuser', views.authenticate_user, name='loginuser'),

    path('pay', views.mpesastkcall, name='mpesa'),


]
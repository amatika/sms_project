from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from  .models import Myuser,Student


def registration(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def mypage(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def courses(request):
  template = loader.get_template('courses.html')
  return HttpResponse(template.render())

def login(request):
  #template = loader.get_template('login.html')
  #return HttpResponse(template.render())
  return render(request, 'login.html')

def dashboard(request):
  data=Student.objects.all();
  context = {'data':data}
  return render(request, 'dashboard.html',context)

def coursedashboard(request):
  template = loader.get_template('coursedash.html')
  return HttpResponse(template.render())

#@csrf_protect

@csrf_exempt
def adduser(request):
  template = loader.get_template('login.html')
  if request.method == 'POST':
    name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mydata={'name':name,'email':email,'password':password}
    print(mydata)
    query=Myuser(username=name,email=email,password=password)
    query.save()
  return HttpResponse(template.render())


@csrf_exempt
def addstudent(request):
  if request.method == 'POST':
    formname = request.POST.get('studname')
    formemail = request.POST.get('studmail')
    formage = request.POST.get('studage')

    obj1=Student(studentname=formname,email=formemail,age=formage)
    obj1.save()

    # fetch the student data to be displayed
  mydata = Student.objects.all()
  context = {'data': mydata}
  return render(request, 'dashboard.html', context)




















def editstudent(request,id):
  data = Student.objects.get(id=id);
  context = {'data': data}
  return render(request, 'updatestudent.html', context)

def updatestudent(request,id):
  if request.method == 'POST':
    name = request.POST.get('studname')
    email = request.POST.get('studmail')
    age = request.POST.get('studage')

    #modify the student details based on the student id given
    editstudent = Student.objects.get(id=id)
    editstudent.studentname=name
    editstudent.email=email
    editstudent.age=age
    editstudent.save()
  return redirect('/dashboard')

def deletestudent(request,id):
  deletestudent = Student.objects.get(id=id)
  deletestudent.delete()
  return redirect('/dashboard')
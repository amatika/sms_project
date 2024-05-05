from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from  .models import Myuser,Student,Course
from .forms import StudentForm,CourseForm
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
import requests
import json

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
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
  return render(request, 'login.html')

def dashboard(request):
  data=Student.objects.all()
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
  data = Student.objects.get(id=id)
  context = {'data': data}
  return render(request, 'updatestudent.html', context)

def updatestudent(request,id):
  if request.method == 'POST':
    name = request.POST.get('studname')
    email = request.POST.get('studmail')
    age = request.POST.get('studage')

    #modify the student details based on the student id given
    editstudent = Student.objects.get(id=id)#here  fetch the student to be changed

    #i make changes based on what came from the database
    editstudent.studentname=name
    editstudent.email=email
    editstudent.age=age
    #here i am saving the changes
    editstudent.save()

  #here i want to display the new changes in my html table so i fetchh them from my database table
  thedata = Student.objects.all()
  #here i create a dictionary to hold the fetched info
  context = {'data': thedata}
  #here i now pass the ftched info back to my dashoard
  return render(request, 'dashboard.html', context)


  #return redirect('/dashboard')

def deletestudent(request,id):
  deletestudent = Student.objects.get(id=id)
  deletestudent.delete()
  return redirect('/dashboard')

def gettestform(request):
  if request.method == 'POST':
    theform=StudentForm(request.POST)
    if theform.is_valid():
      theform.save()
      return HttpResponse("Student added successfully")
  form=StudentForm()
  context={"form":form}
  return render(request, 'testform.html',context)

def create_course(request):
    form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


def success(request):
  courses = Course.objects.all()
  return render(request, 'success.html', {'courses': courses})



def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
      form = CourseForm(request.POST, instance=course)
      if form.is_valid():
        form.save()
        return redirect('success')
    else:
      form = CourseForm(instance=course)
    return render(request, 'update_course.html', {'form': form})


def delete_course(request, pk):
  course = get_object_or_404(Course, pk=pk)
  if request.method == 'POST':
    course.delete()
    return redirect('success')
  return render(request, 'delete_course.html', {'course': course})

def create_course22(request):
    if request.method == 'POST':
      form = CourseForm(request.POST)
      if form.is_valid():
        form.save()
        # Redirect to a success page
        return redirect('success')
    else:
      form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

@csrf_exempt
def authenticate_user(request):
  if request.method=="POST":
    usermail = request.POST.get('myemail')
    password = request.POST.get('mypassword')

  users = Myuser.objects.filter(email=usermail)
  # Check if any user with the given email exists
  if users.exists():
    # Iterate over each user with the given email
    for user in users:
      # Check f the password matches
      if user.password==password:
        print("success")
        return redirect("/dashboard")
  # If no user with the given email or password match, return None
  return redirect("/thelogin")


#def mpesastkcall(request):
"""  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ksu1zTTHCUaHRX06HiuK7AgGIPkd'
  }

  payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNTA1MDEzOTE1",
    "Timestamp": "20240505013915",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254792774536,
    "PartyB": 174379,
    "PhoneNumber": 254708374149,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X"
  }
  payload_json = json.dumps(payload)
  response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',headers=headers, data=payload_json)
  print(response.text.encode('utf8'))
"""
def mpesastkcall(request):
  cl = MpesaClient()
  phone_number = '0794512054'
  amount = 1
  account_reference = 'reference'
  transaction_desc = 'Description'
  callback_url = 'https://darajambili.herokuapp.com/express-payment';
  response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
  return HttpResponse(response)
  #return HttpResponse(response.text.encode('utf8'))





def stk_push_callback(request):
  data = request.body

  return HttpResponse("STK Push in Django👋")



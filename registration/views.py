from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from  .models import Myuser,Student,Course
from registration.forms import StudentForm
from .forms import StudentForm,CourseForm
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
    if request.method == 'POST':
      form = CourseForm(request.POST)
      if form.is_valid():
        form.save()
        # Redirect to a success page
        return redirect('success')
    else:
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
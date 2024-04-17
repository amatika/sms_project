from django.db import models
class Myuser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False,blank=False)

class Course(models.Model):
    coursename = models.CharField(max_length=100)
    description=models.TextField()

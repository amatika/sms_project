from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
class Myuser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False,blank=False)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.title
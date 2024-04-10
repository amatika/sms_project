from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def coursesView(request):
    template=loader.get_template("courses.html")
    return HttpResponse(template.render())
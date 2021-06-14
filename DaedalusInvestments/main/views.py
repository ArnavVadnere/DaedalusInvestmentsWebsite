from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, "main/home.html")

def aboutus(response):
    return render(response, "main/aboutus.html")

def investmentstrategy(response):
    return render(response, "main/investmentstrategy.html")

def education(response):
    return render(response, "main/education.html")

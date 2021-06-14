from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutus/", views.aboutus, name="About_Us"),
    path("investmentstrategy/", views.investmentstrategy, name="investmentstrategy"),
    path("education/", views.education, name="Education")
]
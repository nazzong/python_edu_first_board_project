from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) :
    return render(request, "core/home.html")

def assignment(request) :
    return render(request, "core/assignment.html")

def service(request) :
    return render(request, "core/service.html")

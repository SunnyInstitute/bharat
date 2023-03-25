from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello worlds")
def about (request):
    return HttpResponse("about uspage")
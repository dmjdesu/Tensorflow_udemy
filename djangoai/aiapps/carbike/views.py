from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Good Night World")

def predict(request):
	return HttpResponse("Show predictions")


# Create your views here.

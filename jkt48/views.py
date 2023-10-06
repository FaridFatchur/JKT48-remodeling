from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'jkt48/home.html')

def members(request):
    return render(request, 'jkt48/members.html')
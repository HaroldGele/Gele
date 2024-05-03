from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
# Create your views here.

def home(request):
    #DO SOMETHING

    return render(request, 'home.html')


def register(request):

    return render(request, 'register.html')
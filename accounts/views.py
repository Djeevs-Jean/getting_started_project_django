from django.http import HttpResponse
from django.shortcuts import render, redirect

def login(request):
    context = {
        'title': 'Account Login'
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    context = {
        'title': 'Account Login'
    }
    return render(request, 'accounts/register.html', context)
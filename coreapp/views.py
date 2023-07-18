from django import http
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def browser_auth(request):
    next_url = request.GET.get('next', '/shops/')
    if request.user.is_authenticated:
        return http.JsonResponse({
            'next': next_url,
            'alreadyLoggedIn': True
        })
    user_object = authenticate(request)
    if user_object is None:
        messages.error(request, "Unable to login! Please try again.")
        return http.JsonResponse({
            'next': '/shops/',
            'error': True,
            'message': 'Unable to login! Please try again.'
        })
    login(request, user_object)
    return http.JsonResponse({
        'next': '/shops/'
    })


def app_logout(request):
    logout(request)
    return redirect('/shops/')
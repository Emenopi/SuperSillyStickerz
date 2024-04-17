from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.models import Shopper, Order

def index(request):
    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    response = render(request, 'stickerz/index.html', context=context_dict)
    return response

def custom_sticker(request):
    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    response = render(request, 'stickerz/custom_sticker.html', context=context_dict)
    return response

def dashboard(request):

    user = User.objects.first()
    shopper = Shopper.objects.get(user=user)
    orders = Order.objects.filter(shopper=shopper)

    context_dict = {}
    context_dict['shopper'] = shopper
    context_dict['orders'] = orders 
    
    response = render(request, 'stickerz/dashboard.html', context=context_dict)
    return response


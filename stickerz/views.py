from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.models import Sticker

def index(request, category=None):
    context_dict = {}

    categories = []

    stickers = Sticker.objects.all()
    for sticker in stickers:
        if sticker.category not in categories and sticker.category!="custom":
            categories.append(sticker.category)
        

    context_dict['categories'] = categories


    # if no cateogory specified it is the homepage
    if category == None:
        context_dict['stickers'] = Sticker.objects.exclude(category="custom") # so users custom stickers arent availiable generally
    else:
        context_dict['stickers'] = Sticker.objects.filter(category=category)
    
    response = render(request, 'stickerz/index.html', context=context_dict)
    return response

def sticker(request, sticker_slug):
    context_dict = {}
    try:
        category = Sticker.objects.get(sticker_slug=sticker_slug)
        context_dict['category'] = category
    except Sticker.DoesNotExist:
        context_dict['blah'] = None
    return render(request, 'stickerz/sticker.html', context=context_dict)
 

def custom_sticker(request):
    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    response = render(request, 'stickerz/custom_sticker.html', context=context_dict)
    return response
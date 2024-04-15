from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.forms import CustomStickerForm, CustomStickerOrderForm
from datetime import *
from stickerz.models import Sticker

def index(request):
    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    response = render(request, 'stickerz/index.html', context=context_dict)
    return response

def custom_sticker(request):
    custom_sticker_form = CustomStickerForm()
    custom_sticker_order_form = CustomStickerOrderForm()


    if request.method == 'POST':
        custom_sticker_form = CustomStickerForm(request.POST)
        custom_sticker_order_form = CustomStickerOrderForm(request.POST)
        if custom_sticker_form.is_valid() and custom_sticker_order_form.is_valid():
            custom_sticker = custom_sticker_form.save(commit=False)
            custom_sticker.name = "custom-sticker" + str(datetime.now())
            custom_sticker.price = 2.00
            custom_sticker.category = "Custom"
            custom_sticker.save()

            custom_sticker_order = custom_sticker_order_form.save(commit=False)
            custom_sticker_order.sticker = Sticker.objects.get(pk=custom_sticker.id)
            
            custom_sticker_order.status = "Processing"

            from stickerz.models import Shopper
            custom_sticker_order.shopper = Shopper.objects.first()


            # temporary while login doesn't exist
            custom_sticker_order = custom_sticker_order.save()

            

            return redirect('/stickerz/')        
        else:
            print(custom_sticker_order_form.errors, custom_sticker_form.errors)


    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    context_dict['custom_sticker_order_form'] = custom_sticker_order_form
    context_dict['custom_sticker_form'] = custom_sticker_form
    response = render(request, 'stickerz/custom_sticker.html', context=context_dict)
    return response

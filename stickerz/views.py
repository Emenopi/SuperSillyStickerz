from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.forms import CustomStickerForm, CustomStickerOrderForm, RegisterForm, ShopperForm, UserForm
from datetime import *
from stickerz.models import Shopper, Sticker



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
            custom_sticker_order.shopper = Shopper.objects.get(user=request.user)
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

def billing(request):

    shopper_form = ShopperForm(request.POST)
    if request.method =='POST':
        if shopper_form.is_valid():
            shopper = shopper_form.save(commit=False)
            shopper.user = User.objects.get(username=request.user.username)
            shopper.save()
            return redirect(reverse('stickerz:index'))
        else:
            print("invalid shopping")
            return print(shopper_form.errors)

    response = render(request, 'stickerz/billing.html', context={
                                                            'shopper_form': shopper_form,
                                                       })
    return response

def user_login(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if 'login' in request.POST:
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)   

            if user:
                login(request, user)
                return redirect(reverse('stickerz:index'))
            else:
                print(f"Invalid login details: {username}, {password}")

        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            if register_form.is_valid():
                user = register_form.save()
                user.set_password(user.password)
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect(reverse('stickerz:billing'))   
        else:
            register_form = RegisterForm()
     
    
    return render(request, 'stickerz/login.html', context={
                                                            'register_form': register_form,
                                                        })

def user_logout(request):
    logout(request)
    return redirect(reverse('stickerz:index'))


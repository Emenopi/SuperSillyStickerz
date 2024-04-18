from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.forms import RegisterForm, ShopperForm, OrderForm
from stickerz.models import Shopper, Sticker, Order



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
        sticker = Sticker.objects.get(sticker_slug=sticker_slug)
        context_dict['sticker'] = sticker
    except Sticker.DoesNotExist:
        context_dict['sticker'] = None


    order_form = OrderForm(request.POST)
    context_dict['order_form'] = order_form
    if request.method =='POST':
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.shopper = Shopper.objects.get(user = User.objects.get(username=request.user.username))
            order.sticker = sticker
            order.status = "Processing"
            order.save()
            return redirect(reverse('stickerz:index'))
        else:
            print("invalid shopping")
            return print(order_form.errors)
        
    return render(request, 'stickerz/sticker.html', context=context_dict)
 

def custom_sticker(request):
    context_dict = {}
    context_dict['title'] = "Super Silly Stickerz!"
    response = render(request, 'stickerz/custom_sticker.html', context=context_dict)
    return response

def dashboard(request):
    user = User.objects.get(username=request.user.username)
    shopper = Shopper.objects.get(user=user)
    orders = Order.objects.filter(shopper=shopper)

    context_dict = {}
    context_dict['shopper'] = shopper
    context_dict['orders'] = orders 
    
    response = render(request, 'stickerz/dashboard.html', context=context_dict)
    return response

def edit_billing(request):
    shopper_form = ShopperForm(request.POST)
    if request.method =='POST':
        if shopper_form.is_valid():
            new_shopper = shopper_form.save(commit=False)

            # set known data
            shopper = Shopper.objects.get(user = request.user)
            new_shopper.id = shopper.id
            new_shopper.user = shopper.user

            #set data from form
            shopper.shippingFName = new_shopper.shippingFName
            shopper.shippingLName = new_shopper.shippingLName
            shopper.shippingAddress = new_shopper.shippingAddress
            shopper.shippingCountry = new_shopper.shippingCountry
            shopper.shippingPostcode = new_shopper.shippingPostcode
            shopper.billingFName = new_shopper.billingFName
            shopper.billingLName = new_shopper.billingLName
            shopper.billingAddress = new_shopper.billingAddress
            shopper.billingCountry = new_shopper.billingCountry
            shopper.billingPostcode = new_shopper.billingPostcode
            shopper.cardNo = new_shopper.cardNo
            shopper.expiration = new_shopper.expiration # expiration is only month and year and no ambiguity on century eg 12/24 not 12/2024
            shopper.cvv = new_shopper.cvv

            #update
            shopper.save()
            return redirect(reverse('stickerz:dashboard'))
        else:
            print("invalid shopping")
            return print(shopper_form.errors)

    response = render(request, 'stickerz/edit_billing.html', context={
                                                            'shopper_form': shopper_form,
                                                       })
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


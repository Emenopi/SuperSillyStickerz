from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stickerz.forms import RegisterForm, BillingForm, ShippingForm, UserForm
from stickerz.models import Shopper


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

def billing(request):

    shipping_form = ShippingForm()
    billing_form = BillingForm()
    
    if request.method =='POST':
        if billing_form.is_valid() and shipping_form.is_valid():
            shopper = Shopper.objects.get_or_create(user=request.user)
            shopper.shippingFName = shipping_form.shippingFName
            shopper.shippingLName = shipping_form.shippingLName
            shopper.shippingAddress = shipping_form.shippingAddress
            shopper.shippingCountry = shipping_form.shippingCountry
            shopper.shippingPostcode = shipping_form.shippingPostcode
            shopper.billingFName = billing_form.billingFName
            shopper.billingLName = billing_form.billingLName
            shopper.billingAddress = billing_form.billingAddress
            shopper.billingCountry = billing_form.billingCountry
            shopper.billingPostcode = billing_form.billingPostcode
            shopper.cardNo = billing_form.cardNo
            shopper.expiration = billing_form.expiration
            shopper.cvv = billing_form.cvv
            shopper.save()
            return redirect(reverse('stickerz:index'))
        else:
            return HttpResponse(billing_form.errors, shipping_form.errors)

    response = render(request, 'stickerz/billing.html', context={
                                                            'shipping_form': shipping_form,
                                                            'billing_form': billing_form
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


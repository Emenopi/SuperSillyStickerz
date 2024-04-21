from django import forms
from stickerz.models import Sticker, Shopper, Order
from django.contrib.auth.models import User

FINISHES = (
        ('matte', 'Matte'),
        ('gloss', 'Gloss'),
        ('semi-gloss', 'Semi-gloss'),
        ('transparent', 'Transparent'),
        ('holographic', 'Holographic'),
    )

class CustomStickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = ('image', )

class CustomStickerOrderForm(forms.ModelForm):
    finish = forms.ChoiceField(choices=FINISHES)

    class Meta:
        model = Order
        fields = ('finish', 'quantity', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
 
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class ShopperForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = ('shippingFName', 'shippingLName',
                  'shippingAddress', 'shippingCountry',
                  'shippingPostcode',
                  'billingFName', 'billingLName',
                  'billingAddress', 'billingCountry',
                  'billingPostcode', 'cardNo',
                  'expiration', 'cvv')

class OrderForm(forms.ModelForm):
    finish = forms.ChoiceField(choices=FINISHES)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'min': '1'}))
    
    class Meta:
        model = Order
        fields = ('finish', 'quantity')



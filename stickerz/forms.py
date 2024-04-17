from django import forms
from stickerz.models import Sticker, Shopper
from django.contrib.auth.models import User

class CustomStickerForm(forms.ModelForm):
    #image = forms.ImageField()
    class Meta:
        model = Shopper
        fields = ('website', 'customSticker',)

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




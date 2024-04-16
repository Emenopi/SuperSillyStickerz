from django import forms
from stickerz.models import Sticker, Shopper
from django.contrib.auth.models import User

class CustomStickerForm(forms.ModelForm):
    #image = forms.ImageField()
    class Meta:
        model = Shopper
        fields = ('website', 'customSticker',)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
 
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = ('shippingFName', 'shippingLName',
                  'shippingAddress', 'shippingCountry',
                  'shippingPostcode')
        
class BillingFormFull(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = ('billingFName',
                  'billingLName', 'billingAddress',
                  'billingCountry', 'billingPostcode',
                  'cardNo', 'expiration', 'cvv')
        
class BillingForm_cardOnly(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = ('cardNo', 'expiration', 'cvv')





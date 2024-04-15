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





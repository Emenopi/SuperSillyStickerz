from django import forms
from stickerz.models import Sticker, Shopper, Customise
from django.contrib.auth.models import User
from stickerz import Shopper

class CustomStickerForm(forms.ModelForm):
    #image = forms.ImageField()
    class Meta:
        model = Shopper
        fields = ('website', 'picture',)
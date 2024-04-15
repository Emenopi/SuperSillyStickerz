from django import forms
from stickerz.models import Sticker, Shopper, Order
from django.contrib.auth.models import User
from stickerz.models import Shopper

class CustomStickerForm(forms.ModelForm):

    #image = forms.ImageField()
    class Meta:
        model = Sticker
        fields = ('image', )

class CustomStickerOrderForm(forms.ModelForm):
    CHOICES = (
        ('matte', 'Matte'),
        ('gloss', 'Gloss'),
        ('semi-gloss', 'Semi-gloss'),
        ('transparent', 'Transparent'),
        ('holographic', 'Holographic'),
    )
    finish = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Order
        fields = ('finish', 'quantity', )
    # forms.py



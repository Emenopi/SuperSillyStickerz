from django.contrib import admin
from stickerz.models import Shopper, Sticker

class ShopperAdmin(admin.ModelAdmin):
    list_display = ('user', 'shippingFName', 'shippingLName', 'shippingAddress', 'shippingCountry', 'billingFName', 'cardNo' )
    
admin.site.register(Sticker)

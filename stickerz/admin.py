from django.contrib import admin
from stickerz.models import Shopper, Sticker

# Register your models here.
class ShopperAdmin(admin.ModelAdmin):
    list_display = ('user', 'shippingFName', 'shippingLName', 'shippingAddress', 'shippingCountry', 'billingFName', 'cardNo' )

admin.site.register(Shopper, ShopperAdmin)
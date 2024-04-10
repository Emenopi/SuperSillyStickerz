from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Sticker(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='sticker_images', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=40)
    sticker_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.sticker_slug = slugify(self.name)
        super(Sticker, self).save(*args, **kwargs)
        # Modified save function to update sticker_slug to be the slugified name of the sticker

    def __str__(self):
        return self.name

class Shopper(models.Model):
    # Links UserProfile to a User model instance.
    # includes username, password, email, firstname, & lastname
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    customSticker = models.ImageField(upload_to='custom_sticker_images', blank=True)

    # primary key ID is built in

    # shipping
    shippingFName = models.CharField(max_length=64)
    shippingLName = models.CharField(max_length=64)
    shippingAddress = models.CharField(max_length=512)
    shippingCountry = models.CharField(max_length=64)
    shippingPostcode = models.CharField(max_length=8)

    # billing
    billingFName = models.CharField(max_length=64)
    billingLName = models.CharField(max_length=64)
    billingAddress = models.CharField(max_length=512)
    billingCountry = models.CharField(max_length=64)
    billingPostcode = models.CharField(max_length=8)
    cardNo = models.CharField(max_length=16)
    expiration = models.CharField(max_length=4) # expiration is only month and year and no ambiguity on century eg 12/24 not 12/2024
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username # userid will be shown in admin dashboard for each entry

    def save(self, *args, **kwargs):
        if not self.user or not self.id: # userid and primary key won't be encryted
            #encrypt everything else with same encryption as password
            self.shippingFName = make_password(self.shippingFName)
            self.shippingLName = make_password(self.shippingFName)
            self.shippingAddress = make_password(self.shippingAddress)
            self.shippingCountry = make_password(self.shippingCountry)
            self.shippingPostcode = make_password(self.shippingPostcode)

            self.billingFName = make_password(self.billingFName)
            self.billingLName = make_password(self.billingLName)
            self.billingAddress = make_password(self.billingAddress)
            self.billingCountry = make_password(self.billingCountry)
            self.billingPostcode = make_password(self.billingPostcode)
            self.cardNo = make_password(self.cardNo)
            self.expiration = make_password(self.expiration)
            self.cvv = make_password(self.cvv)
        # save after encryption
        super(Shopper, self).save(*args, **kwargs)

class Order(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    finish = models.CharField(max_length=40)
    quantity = models.IntegerField()
    timePlaced = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Sticker(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='sticker_images')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    finish = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    sticker_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        sticker_slug = slugify(self.name)
        super(Sticker, self).save(*args, **kwargs)
        # Modified save function to update sticker_slug to be the slugified name of the sticker

    def __str__(self):
        return self.name

class Shopper(models.Model):
    # Links UserProfile to a User model instance.
    # includes username, password, email, firstname, & lastname
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
    cardNo = models.CharField(max_length=12)
    expiration = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.shippingFName

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.pk and not self.user:
            self.shippingFName = make_password(self.shippingFName, True)
            self.shippingLName = make_password(self.shippingFName, True)
            self.shippingAddress = make_password(self.shippingAddress, True)
            self.shippingCountry = make_password(self.shippingCountry, True)
            self.shippingPostcode = make_password(self.shippingPostcode, True)

            self.billingFName = make_password(self.billingFName, True)
            self.billingLName = make_password(self.billingLName, True)
            self.billingAddress = make_password(self.billingAddress, True)
            self.billingCountry = make_password(self.billingCountry, True)
            self.billingPostcode = make_password(self.billingPostcode, True)
            self.cardNo = make_password(self.cardNo, True)
            self.expiration = make_password(self.expiration, True)
            self.cvv = make_password(self.cvv, True)
            self.save()
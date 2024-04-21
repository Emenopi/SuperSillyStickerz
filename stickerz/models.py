from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django_cryptography.fields import encrypt

class Sticker(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='sticker_images', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=40)
    sticker_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        self.sticker_slug = slugify(self.name)
        super(Sticker, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Shopper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    shippingFName = encrypt(models.CharField(max_length=64))
    shippingLName = encrypt(models.CharField(max_length=64))
    shippingAddress = encrypt(models.CharField(max_length=512))
    shippingCountry = encrypt(models.CharField(max_length=64))
    shippingPostcode = encrypt(models.CharField(max_length=8))

    billingFName = encrypt(models.CharField(max_length=64))
    billingLName = encrypt(models.CharField(max_length=64))
    billingAddress = encrypt(models.CharField(max_length=512))
    billingCountry = encrypt(models.CharField(max_length=64))
    billingPostcode = encrypt(models.CharField(max_length=8))

    cardNo = encrypt(models.CharField(max_length=16))
    expiration = encrypt(models.CharField(max_length=4)) # DDMM
    cvv = encrypt(models.CharField(max_length=3))



    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):  
        # hashed fields 
        self.cardNo = make_password(self.cardNo)
        self.expiration = make_password(self.expiration)
        self.cvv = make_password(self.cvv)
        super(Shopper, self).save(*args, **kwargs)

class Order(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    finish = models.CharField(max_length=40)
    quantity = models.IntegerField()
    timePlaced = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.utils.text import slugify

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


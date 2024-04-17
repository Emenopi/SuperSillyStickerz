# Generated by Django 2.2 on 2024-04-15 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='sticker_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.CharField(max_length=40)),
                ('sticker_slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('customSticker', models.ImageField(blank=True, upload_to='custom_sticker_images')),
                ('shippingFName', models.CharField(max_length=64)),
                ('shippingLName', models.CharField(max_length=64)),
                ('shippingAddress', models.CharField(max_length=512)),
                ('shippingCountry', models.CharField(max_length=64)),
                ('shippingPostcode', models.CharField(max_length=8)),
                ('billingFName', models.CharField(max_length=64)),
                ('billingLName', models.CharField(max_length=64)),
                ('billingAddress', models.CharField(max_length=512)),
                ('billingCountry', models.CharField(max_length=64)),
                ('billingPostcode', models.CharField(max_length=8)),
                ('cardNo', models.CharField(max_length=16)),
                ('expiration', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
                ('finish', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('timePlaced', models.DateTimeField(auto_now_add=True)),
                ('shopper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stickerz.Shopper')),
                ('sticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stickerz.Sticker')),
            ],
        ),
    ]

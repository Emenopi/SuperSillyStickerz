from django.urls import path
from stickerz import views

app_name = 'stickerz'

urlpatterns = [
    path('', views.index, name='index'),
    path('custom_sticker/', views.custom_sticker, name='custom_sticker'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
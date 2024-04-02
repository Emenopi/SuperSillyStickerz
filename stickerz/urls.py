from django.urls import path
from stickerz import views

app_name = 'stickerz'

urlpatterns = [
    path('', views.index, name='index'),
]
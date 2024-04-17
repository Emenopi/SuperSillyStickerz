from django.urls import path
from stickerz import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'stickerz'

urlpatterns = [
    path('', views.index, name='index'),
    path('custom_sticker/', views.custom_sticker, name='custom_sticker'),
    path('category/<slug:category>/', views.index, name='category'),
    path('sticker/<slug:sticker_slug>/', views.sticker, name='sticker'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
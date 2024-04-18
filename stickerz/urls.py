from django.urls import path
from stickerz import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'stickerz'

urlpatterns = [
    path('', views.index, name='index'),
    path('custom_sticker/', views.custom_sticker, name='custom_sticker'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('billing/', views.billing, name="billing"),
    path('edit-billing/', views.edit_billing, name="edit_billing"),
    path('category/<slug:category>/', views.index, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


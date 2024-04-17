from django.urls import path
from stickerz import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'stickerz'

urlpatterns = [
    path('', views.index, name='index'),
    path('custom_sticker/', views.custom_sticker, name='custom_sticker'),
<<<<<<< HEAD
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('billing/', views.billing, name="billing"),
]
=======
    path('category/<slug:category>/', views.index, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 089220aab13d1eaf6a5a8d01d0b0c1a3b91599d5

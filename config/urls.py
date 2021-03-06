"""config URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('', include('shop.urls', namespace='shop')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('users.urls', namespace='users')),
    path('oauth/', include('social_django.urls', namespace='social')), 
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns+= static(
    settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT) 
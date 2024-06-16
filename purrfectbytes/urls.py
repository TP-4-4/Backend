from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from purrfectbytes.yasg import urlpatterns1
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('users/', include('users.urls', namespace='users')),
    #path('', include('shop.urls', namespace='shop')),
    #path('api/', include('shop.api.urls', namespace='api')),
    #path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += urlpatterns1

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

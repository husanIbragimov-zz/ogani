from django.urls import path, include
from .views import home_view, shop_grid

app_name = 'products'

urlpatterns = [
    path('', home_view),
    path('shop-grid/', shop_grid, name='shop-grid'),

    path('api/', include('apps.products.api.urls')),
]

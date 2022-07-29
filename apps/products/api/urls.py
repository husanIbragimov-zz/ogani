from django.urls import path
from . import views


urlpatterns = [
    path('category/list/', views.CategoryListAPIView.as_view()),
    path('product/list/', views.ProductListAPIView.as_view()),
    path('product-rate/create/', views.RateCreateAPIView.as_view()),
    path('product/views/<int:pk>/', views.UpdateViewsAPIView.as_view()),
]

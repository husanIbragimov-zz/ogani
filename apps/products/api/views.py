from rest_framework import generics, response, status, permissions
from rest_framework.response import Response

from ..models import Category, Product, ProductImage, Rate
from .serializers import CategorySerializer, ProductSerializer, RateSerializer


class CategoryListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/category/list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/product/list/
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        return qs


class RateCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/product-rate/create/
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateViewsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


from rest_framework import serializers
from ..models import Category, Product, ProductImage, Rate


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'view', 'get_mid_rate', 'description', 'product_images']


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['product', 'user', 'rate']
        extra_kwargs = {
            'user': {"required": False}
        }

    def create(self, attrs):
        user = self.context.get('request').user
        instance = Rate.objects.create(**attrs)
        instance.user = user
        instance.save()
        return instance

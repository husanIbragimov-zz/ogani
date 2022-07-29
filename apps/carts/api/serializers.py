from rest_framework import serializers
from ..models import WishList, Cart, CartItem, Order
from ...accounts.serializers import AccountSerializer
from ...products.api.serializers import ProductSerializer


class WishListSerializer(serializers.ModelSerializer):
    user = AccountSerializer(required=False)
    product = ProductSerializer(required=False)

    class Meta:
        model = WishList
        fields = ['id', 'user', 'product']


class WishListCreateSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)

    # product_sz = serializers.SerializerMethodField(read_only=True)

    # def get_product_sz(self, obj):
    #     product = obj.product
    #     product_sz = ProductSerializer(product)
    #     return product_sz.data

    class Meta:
        model = WishList
        fields = ['id', 'user', 'user_email', 'product']  # <-- 'product_sz'
        extra_kwargs = {
            "user": {"required": False}
        }


class CartItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class CartSerializer(serializers.ModelSerializer):
    client = AccountSerializer(read_only=True)
    cart_items = serializers.SerializerMethodField()

    def get_cart_items(self, obj):
        qs = CartItem.objects.filter(cart_id=obj.id)
        sz = CartItemReadSerializer(qs, many=True)
        return sz.data

    class Meta:
        model = Cart
        fields = ['id', 'client', 'is_ordered', 'get_cart_items', 'cart_items', 'get_cart_total']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class OrderSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField(read_only=True)

    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Order
        fields = ['transaction_id', 'cart', 'client', 'phone', 'address', 'note', 'status', 'status_display',
                  'created_at']
        extra_kwargs = {
            'transaction_id': {"read_only": True},
            'cart': {"required": False},
            'client': {"required": False},
        }

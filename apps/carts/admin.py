from django.contrib import admin
from .models import WishList, Cart, CartItem, Order


class CartListInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartListInline]


admin.site.register(WishList)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order)

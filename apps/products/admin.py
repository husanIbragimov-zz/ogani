from django.contrib import admin
from .models import Category, Product, ProductImage, Rate


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, RateInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rate)

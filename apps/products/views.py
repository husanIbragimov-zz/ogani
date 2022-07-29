from django.shortcuts import render
from apps.blog.models import Post, Tag
from .models import Category, Product, ProductImage, Rate
from ..carts.models import WishList


def home_view(request):
    products = Product.objects.all().order_by('-id')
    category = Category.objects.all()
    latest_products = products[:6]
    top_rate_products = products.order_by('-mid_rate')[:6]
    top_viewed_products = products.order_by('-view')[:6]
    blog_latest = Post.objects.order_by('-id')[:3]

    context = {
        'categories': category,
        'products': products[:8],

        'blog_latests': blog_latest,

        'latest_products': latest_products,
        'top_rate_products': top_rate_products,
        'top_viewed_products': top_viewed_products,
    }
    return render(request, 'index.html', context)


def shop_grid(request, pk):
    products = Product.objects.order_by('-id')
    categories = Category.objects.all()
    product = Product.objects.get(id=pk)

    ctx = {
        'categories': categories,
        'last_3_posts': products[:6],
        'products': products,
        'product': product
    }
    try:
        next = Product.objects.get(id=pk+1)
        prev = Product.objects.get(id=pk-1)
        ctx['next'] = next
        ctx['prev'] = prev
    except:
        pass

    return render(request, 'shop-grid.html', ctx)

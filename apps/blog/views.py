from django.shortcuts import render
from .models import Post, Tag
from ..products.models import Category


def blog_list(request):
    blogs = Post.objects.order_by('-id')
    categories = Category.objects.order_by('-id')
    tags = Tag.objects.all()
    ctx = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'blog.html', ctx)


def blog_detail(request, pk):
    blogs = Post.objects.order_by('-id')[:3]
    blog = Post.objects.get(id=pk)
    categories = Category.objects.order_by('-id')
    tags = Tag.objects.all()

    ctx = {
        'blog': blog,
        'categories': categories,
        'tags': tags,
        'blogs': blogs,
    }
    return render(request, 'blog-details.html', ctx)

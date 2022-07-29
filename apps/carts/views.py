from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
# from openid import message

from .models import WishList, Cart, CartItem
from ..products.models import Product, Category
from .forms import OrderForm


def add_wishlist(request):
    pid = request.GET.get('_pid')
    product = Product.objects.get(id=pid)
    user = request.user
    wishlist_count = WishList.objects.filter(user=user, product=product).count()
    if wishlist_count < 1:
        WishList.objects.create(user=user, product=product)
        data = {
            'success': True,
            'product': product.name
        }
    else:
        WishList.objects.get(user=user, product=product).delete()
        data = {
            'success': False,
            'message': 'Already removed from your wishlist',
            'product': product.name
        }
    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def my_wishlist(request):
    my_wlist = WishList.objects.filter(user=request.user)
    categories = Category.objects.all()
    ctx = {
        'products': my_wlist,
        'categories': categories,
    }
    return render(request, 'my-wishlist.html', ctx)


def add_cart(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    print(product)
    my_cart, new_cart = Cart.objects.get_or_create(client=user, is_ordered=False)
    data = None
    if my_cart:
        CartItem.objects.create(product=product, cart=my_cart)
        data = {
            'success': True,
            'product': product.name,
        }
    if new_cart:
        CartItem.objects.create(product=product, cart=new_cart)
        data = {
            'success': True,
            'product': product.name
        }

    return JsonResponse(data, status=201)


def my_cart_view(request):
    categories = Category.objects.all()
    cart, cart = Cart.objects.get_or_create(client=request.user, is_ordered=False)
    ctx = {
        'categories': categories,
        'cart': cart
    }
    return render(request, 'shoping-cart.html', ctx)


def plus_quantity(request):
    ciid = request.GET.get('_ciid')

    cart_item = CartItem.objects.get(id=ciid)
    cart_item.quantity += 1
    cart_item.save()
    data = {'success': True, 'message': 'cart item incremented by one', 'cart_item': cart_item.get_total}
    return JsonResponse(data, status=200)


def minus_quantity(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id=ciid)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        data = {
            'success': True,
            'message': 'cart item decremented by one'
        }
    else:
        cart_item.delete()
        data = {
            'success': True,
            'deleted': True,
            'message': 'cart item was deleted'
        }
    return JsonResponse(data, status=200)


def delete_cart_item_view(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id=ciid)

    cart_item.delete()
    data = {
        'success': True,
        'deleted': True,
        'message': 'cart item was deleted'
    }

    return JsonResponse(data, status=200)


def checkout_view(request):
    categories = Category.objects.all()
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    form = OrderForm()
    is_ordered = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.cart = cart
            order.client = request.user
            order.save()
            cart.is_ordered = True
            is_ordered = True
            cart.save()
            message.success(request, 'Successfully ended!!!')
            return redirect('.')
    ctx = {
        'categories': categories,
        'is_ordered': is_ordered,
        'cart': cart,
        'form': form,
    }
    return render(request, 'checkout.html', ctx)


def cart_view(APIVIEW):
    pass


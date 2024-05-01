from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': datetime.now()})
    items = cart.items.all()
    total = sum(item.quantity * item.unit_price for item in items)
    context = {
        'cart': cart,
        'total': total
    }
    return render(request, 'cart/usercart.html', context)

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': datetime.now()})
    return render(request, 'cart/usercart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'unit_price': product.price})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:cart_detail')

@login_required
def change_item_quantity(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart:cart_detail')
    return redirect('cart:cart_detail')

@login_required
def confirm_order(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, created_at=timezone.now())
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        context = {
            'order': order,
        }
        
        cart.items.all().delete()
        return render(request, 'cart/order-confirmation.html', context)


    return render(request, 'cart/checkout.html')

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'cart/order-confirmation.html', {'order': order})

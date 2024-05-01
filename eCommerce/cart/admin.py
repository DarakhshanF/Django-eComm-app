from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
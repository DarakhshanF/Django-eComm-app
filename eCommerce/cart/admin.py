from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('order_number',)


admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path('', views.cart, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('change/<int:item_id>/', views.change_item_quantity, name='change_item_quantity'),

    path('confirm-order/', views.confirm_order, name='confirm_order'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    # path('checkout/', views.change_item_quantity, name='checkout'),
    # path('order-confirmation/<int:order_id>/', views.confirm_order, name='confirm_order'),
]
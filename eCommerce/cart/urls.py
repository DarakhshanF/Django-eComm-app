from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path('', views.cart, name='cart_detail'),
    # path('', views.cart_detail, name='cart_detail'),
    # path('register/', views.registration.as_view(), name='register'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('change/<int:item_id>/<int:quantity>/', views.change_item_quantity, name='change_item_quantity'),
    path('change/<int:item_id>/', views.change_item_quantity, name='change_item_quantity'),
]
from django.urls import path
from cart.views import cart_products, remove_from_cart, update_quantity

urlpatterns = [
    path('', cart_products, name='cart.products'),
    path('remove/<int:id>', remove_from_cart, name='cart.remove'),
    path('update/<int:id>/<str:action>', update_quantity, name='cart.update_quantity'),
]

from django.shortcuts import render, redirect
from products.models import Products
from decimal import Decimal

def cart_products(req):
    products = Products.objects.filter(incart=True)
    total = sum((product.price or Decimal('0.00')) * product.cart_quantity for product in products)
    tax = total * Decimal('0.08')
    shipping = Decimal('10.00') if total > 0 else Decimal('0.00')
    context = {
        'products_in_cart': products,
        'total': total,
        'shipping': shipping,
        'tax': tax,
        'grand_total': total + shipping + tax,
        'items_count': sum(product.cart_quantity for product in products)
    }
    req.session['cart_count'] = context['items_count']
    return render(req, 'cart/cart.html', context)

def remove_from_cart(req, id):
    product = Products.objects.get(id=id)
    product.incart = False
    product.cart_quantity = 1
    product.save()
    return redirect('cart.products')

def update_quantity(req, id, action):
    product = Products.objects.get(id=id)
    if action == 'increase':
        if product.cart_quantity < product.quantity:
            product.cart_quantity += 1
    elif action == 'decrease' and product.cart_quantity > 1:
        product.cart_quantity -= 1
    product.save()
    return redirect('cart.products')

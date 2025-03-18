from django.shortcuts import render

# Create your views here.


def cart_page(req):
  return   render(req,'cart/cart.html')

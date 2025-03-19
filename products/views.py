from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal

def products_home(request):
    return render(request, "products/home.html",
                  context={"products":Products.objects.filter(active = True)},
                  status=200)

def product_profile(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, "products/details.html", context={"product": product})

def add_product(req):
    if req.method == 'POST':
        namepr = req.POST.get('namepr', '')
        quantitypr = req.POST.get('quantitypr', 0)  
        descriptionpr = req.POST.get('descriptionpr', '')
        pricepr = req.POST.get('pricepr', '0.00')
        imagepr = req.FILES.get('imagepr')

        if imagepr:
            Products.objects.create(
                name=namepr, 
                quantity=quantitypr, 
                description=descriptionpr, 
                image=imagepr,
                price=Decimal(pricepr)
            )

    return render(req, 'products/add.html')

def delete_product(req,id):
    Products.objects.filter(id=id).update(active=False)
    return redirect('products.home')

def update_product(req, id):
    context = {}
    product = Products.objects.get(id=id)
    context['oldPR'] = product

    if req.method == 'POST':
        product.name = req.POST.get('namepr', product.name)
        product.quantity = req.POST.get('quantitypr', product.quantity)
        product.description = req.POST.get('descriptionpr', product.description)
        product.price = Decimal(req.POST.get('pricepr', str(product.price or '0.00')))
        
        if 'imagepr' in req.FILES:
            product.image = req.FILES['imagepr']
            
        product.save()
        return redirect('products.home')

    return render(req, 'products/update.html', context)

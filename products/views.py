from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from django.shortcuts import render, get_object_or_404 , redirect
# from django.http import HttpResponseRedirect 
products = [
    {
        'id': 1,
        'name': 'laptop',
        'price': 1000,
        "image":"mac.png"
    },
    {
        'id': 2,
        'name': 'mobile',
        'price': 500,
        "image":"ip16.jpg"
    },
    {
        'id': 3,
        'name': 'tablet',
        'price': 300,
        "image":"ipad.jpg"
    }
]

def products_home(request):
    # return with template 
    return render(request, "products/home.html",
                #   context={"products":Products.objects.all()} 
                  context={"products":Products.objects.filter(active = True)} 
                
                  ,status=200) # also return with http response

def product_profile(request, id):
    # Use Django's get_object_or_404 to fetch the product or return a 404 response
    product = get_object_or_404(Products, id=id)
    
    # Pass the filtered product to the template
    return render(request, "products/details.html", context={"product": product})


def add_product(req):
    print("method:::", req.method, "::has::", req.POST)
    print("FILES:::", req.FILES)  # ✅ Debugging file uploads

    if req.method == 'POST':
        namepr = req.POST.get('namepr', '')
        quantitypr = req.POST.get('quantitypr', 0)  
        descriptionpr = req.POST.get('descriptionpr', '')
        imagepr = req.FILES.get('imagepr')  # ✅ Use .get() to avoid KeyError

        print("Uploaded image:", imagepr)  # ✅ Debugging

        if imagepr:
            Products.objects.create(
                name=namepr, quantity=quantitypr, description=descriptionpr, image=imagepr
            )
        else:
            print("🚨 No image uploaded!")  # ✅ Debugging

    return render(req, 'products/add.html')

def delete_product(req,id):

         
     Products.objects.filter(id=id).update(active=False)
     
    #  return render (req,'products/update.html')
    #  return HttpResponseRedirect ('/products/')
     return redirect ( 'products.home')

def update_product(req, id):
    context = {}
    product = Products.objects.get(id=id)
    context['oldPR'] = product

    if req.method == 'POST':
        # Get the current values or new values if provided
        product.name = req.POST.get('namepr', product.name)
        product.quantity = req.POST.get('quantitypr', product.quantity)
        product.description = req.POST.get('descriptionpr', product.description)
        
        # Handle image update
        if 'imagepr' in req.FILES:
            product.image = req.FILES['imagepr']
            
        # Save the instance
        product.save()
        return redirect('products.home')

    return render(req, 'products/update.html', context)
     


# Create your views here.

# function views 

# def hello(request): # accepts http request and returns http response
#     print(request)
#     # <WSGIRequest: GET '/helloworld/'>
#     return HttpResponse('Hello we are here')


# def welcome(request):
#     name = 'ahmed'
#     return HttpResponse(f"<h1 style='color:red'>Welcome to Django {name} </h1>")






# def landingPage(request):
#     return HttpResponse(products)


# def product_details(request,id):
#     # id = int(id)
#     filtered = filter(lambda product:product['id'] == id , products)
#     print(filtered)
#     all_products = list(filtered)
#     print(all_products)
    
#     if all_products:
#         print(all_products)
#         print(all_products[0])
#         return HttpResponse(all_products[0]) # 
#     return HttpResponse('Product not found')

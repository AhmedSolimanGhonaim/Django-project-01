from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function views 

def hello(request): # accepts http request and returns http response
    print(request)
    # <WSGIRequest: GET '/helloworld/'>
    return HttpResponse('Hello we are here')


def welcome(request):
    name = 'ahmed'
    return HttpResponse(f"<h1 style='color:red'>Welcome to Django {name} </h1>")

products = [
    {
        'id': 1,
        'name': 'laptop',
        'price': 1000
    },
    {
        'id': 2,
        'name': 'mobile',
        'price': 500
    },
    {
        'id': 3,
        'name': 'tablet',
        'price': 300
    }
]

def landingPage(request):
    return HttpResponse(products)


def product_details(request,id):
    # id = int(id)
    filtered = filter(lambda product:product['id'] == id , products)
    print(filtered)
    all_products = list(filtered)
    print(all_products)
    
    if all_products:
        print(all_products)
        print(all_products[0])
        return HttpResponse(all_products[0])
    return HttpResponse('Product not found')

def products_home(request):
    # return with template 
    return render(request, "products/home.html",
                  context={"products":products} 
                  ,status=200) # also return with http response
    
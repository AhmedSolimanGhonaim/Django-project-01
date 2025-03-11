from django.shortcuts import render
from django.http import HttpResponse

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
                  context={"products":products} 
                  ,status=200) # also return with http response

def product_profile(request,id):
        filtered_products=filter(lambda product: product['id'] == int(id) , products)
        filtered_products = list(filtered_products)
        print("filterd_products ##########")
        if filtered_products:
            product = filtered_products[0]
            return render(request, "products/details.html",  context={"product":product})
        
        return HttpResponse("Product Not Found", status=404) 



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

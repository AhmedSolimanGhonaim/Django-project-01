from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.


featured_products = [
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

def home(request):
    # Add full static path for images
    for product in featured_products:
        product["image_url"] = static(f'home/images/{product["image"]}')

    return render(request, 'home/home.html', {"products": featured_products})


# def featured_home(request):
#     # return with template 
#     print("featured_home")
#     print(featured_products)
#     return render(request, "home/home.html",
#                   context={"products":featured_products} 
#                   ,status=200) # also return with http response
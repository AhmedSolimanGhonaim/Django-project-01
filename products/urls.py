from django.urls import path
from products.views import (products_home , product_profile)

urlpatterns = [
    path('home', products_home , name='products.home'),
    path('<int:id>', product_profile , name="products.profile")
    # path('helloworld', hello, name='home'),
    # path('welc', welcome , name='welcomepage'),
    # path('land', landingPage , name='allproducts'),
    # path('prd/<int:id>', product_details , name='prd.details'),
]

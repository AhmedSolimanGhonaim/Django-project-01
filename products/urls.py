from django.urls import path
from products.views import (products_home , product_profile, update_product , delete_product , add_product )

urlpatterns = [
    path('home', products_home , name='products.home'),
    path('<int:id>', product_profile , name="products.profile"),
    path('update/<int:id>', update_product , name='product.update'),
    path('delete<int:id>', delete_product , name='product.delete'),
    path('add',add_product,name="product.add")
   
    # path('helloworld', hello, name='home'),
    # path('welc', welcome , name='welcomepage'),
    # path('land', landingPage , name='allproducts'),
    # path('prd/<int:id>', product_details , name='prd.details'),
]

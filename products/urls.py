from django.urls import path
from products.views import hello  , welcome , landingPage , product_details

urlpatterns = [
    path('helloworld', hello, name='home'),
    path('welc', welcome , name='welcomepage'),
    path('land', landingPage , name='allproducts'),
    path('prd/<int:id>', product_details , name='prd.details')
]

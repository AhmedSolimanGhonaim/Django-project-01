from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing(request):
     return HttpResponse('Welcome to the categories page')
 
 
 
 
def categories_home(request):
    return render(request, "categories/home.html",status=200)
from django.db import models

# Create your models here.

class Customer (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=100,null= False)
    # insert validation 
    email = models.EmailField(_unique=True,max_length=254)
    # not stored in database but its path stored in db  and infile name media 
    image = models.ImageField(upload_to='customer/imgs', default='customer/imgs/default.jpg')
    createdate = models.DateField(auto_now_add=True)
from django.db import models

# Create your models here.


class Products(models.Model):
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(db_column='Name', max_length=50,null=True)
    image = models.ImageField(upload_to='products/imgs' , default='customer/imgs/default.jpg')
    quantity = models.IntegerField(null=True)
    description=models.CharField(db_column='Description' , max_length=200,null=True )
    active=models.BooleanField(default=True)
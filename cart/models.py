# from django.db import models




# class Products(models.Model):
    
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(db_column='Name', max_length=50,null=True)
#     image = models.ImageField(upload_to='products/imgs' , default='customer/imgs/default.jpg')
#     quantity = models.IntegerField(null=True)
#     description=models.CharField(db_column='Description' , max_length=200,null=True )

# class Cart(models.Model):
#     cart_item_id= models.AutoField(primary_key=True)
#     cart_item_name= models.CharField(db_column='Name', max_length=50) 
#     cart_item_quantity=models.IntegerField(null=False)
#     cart_item_image=models.ImageField(" item image", upload_to=cart/imgs, height_field=None, width_field=None, max_length=None)



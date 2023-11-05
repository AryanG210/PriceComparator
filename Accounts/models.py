from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user_id =  models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False,unique=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

class Brands(models.Model):
    brand_name= models.CharField( max_length=100,primary_key=True)
    brand_logo =  models.ImageField( upload_to='images/Brands', height_field=None, width_field=None, max_length=None)
    brand_website = models.URLField(max_length=300)

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    URL =  models.URLField(max_length=3000)
    product_name = models.CharField( max_length=1000)
    price = models.IntegerField()
    image = models.ImageField( upload_to='images/Products', height_field=None, width_field=None, max_length=1000)
    rating = models.DecimalField(decimal_places=1,max_digits=2,default=0)
    website= models.CharField( max_length=50)

    def __str__(self):
        return self.product_name
    
class Images(models.Model):
    image_name = models.CharField(max_length=50,null=False)
    image = models.ImageField( upload_to='images/Products', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.image_name
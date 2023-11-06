from django.db import models
from django.contrib.auth.models import User
from Accounts.models import Product

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING,primary_key=False)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_id 
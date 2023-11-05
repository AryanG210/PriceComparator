from django.db import models
from django.contrib.auth.models import User
class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    product_id = models.ManyToManyField("Accounts.Product")

    def __str__(self):
        return self.product_id 
from django.db import models

# Create your models here.
class Top_picks(models.Model):
    category = models.CharField( max_length=100)
    product_id = models.ForeignKey("Accounts.Product", on_delete=models.CASCADE)
    refresh_time = models.DateTimeField()

    def __str__(self):
        return str.category
from django.contrib import admin
from Accounts.models import User,Brands,Product
from Home.models import Top_picks
from Cart.models import Cart
# Register your models here.
admin.site.register(User)
admin.site.register(Brands)
admin.site.register(Product)
admin.site.register(Top_picks)
admin.site.register(Cart)
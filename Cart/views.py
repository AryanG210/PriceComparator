from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
import urllib.parse
import json
from .models import Cart
from Accounts.models import Product
from django.db.models import Q
from django.contrib import messages
def cart(request):
    if not User.is_authenticated :
        return HttpResponseRedirect('/user/login')
    user = User.objects.filter(Q(username=request.user.username)).all().first()
    cart = Cart.objects.filter(Q(user_id=user)).all().values('product_id')
    product_ids = [ x['product_id'] for x in cart ]
    items = Product.objects.filter(id__in=product_ids)
    items=list(items.values())
    context = {'items':items, 'user':request.user.username}
    return render(request,'cart.html',context=context)

def addToCart(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            product_encoded = request.body
            decoded_product = urllib.parse.unquote(product_encoded.decode())
            # Split the string at "&csrfmiddlewaretoken" and take the part before it
            parts = decoded_product.split('&csrfmiddlewaretoken')
            result = parts[0]
            try:
                json_string = result.replace('product=', '')
                product = json.loads(json_string)
            except:
                return HttpResponse("Json decode error")
            prod =Product.objects.filter(Q(URL=product['product_link'])).all()
            if(prod.count()==0):
                prod = Product.objects.create(
                    URL=product['product_link'],
                    website = product['website'],
                    rating=float(product['rating']),
                    price=product['price'],
                    product_name = product['name'],
                    image=product['image']
                )
                prod.save()
            else:
                prod=prod.first()
            user = User.objects.filter(Q(username = request.user.username)).first()
            cart= Cart.objects.filter(Q(product_id=prod) & Q(user_id=user)).all()
            if(cart.count()==0):
                cart = Cart.objects.create(user_id=user, product_id=prod)
                cart.save()
            return HttpResponse('Product recieved')
        return HttpResponseRedirect('/user/login')

def DeleteFromCart(request,id):
    if request.user.is_authenticated:
        Cart.objects.filter(Q(id=id)).delete()
        messages.success(request,"Item removed from cart successfully. Refresh page to see changes")

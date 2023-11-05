from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import urllib.parse
def cart(request):
    if not User.is_authenticated :
        return HttpResponseRedirect('/user/login')
    return render(request,'cart.html')

def addToCart(request):
    if request.method =="POST":
        product_encoded = request.body
        product = decoded_data = urllib.parse.unquote(product_encoded.decode())
        product = urllib.parse.parse_qs(product)
        print(product.name)

        return HttpResponse('Product recieved')
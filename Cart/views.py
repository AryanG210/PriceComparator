from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
# Create your views here.
def cart(request):
    if not User.is_authenticated :
        return HttpResponseRedirect('/user/login')
    return render(request,'cart.html')

def addToCart(request):
    if request.method =="POST":
        print(request.POST.get('product'))
        print(request.body)
        # data = json.loads(request.body)
        # product = data.get('product')

        return HttpResponse('Product recieved')
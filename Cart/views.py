from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def cart(request):
    if not User.is_authenticated :
        return HttpResponseRedirect('/user/login')
    return render(request,'cart.html')


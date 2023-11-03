from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def Home(request):
    print(User.is_authenticated)
    context = {'user':'user'} #to put it from the login after the token and all is done
    return render(request,'home.html',context)
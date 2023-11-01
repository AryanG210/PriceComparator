from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {'user':'user'} #to put it from the login after the token and all is done
    return render(request,'home.html',context)
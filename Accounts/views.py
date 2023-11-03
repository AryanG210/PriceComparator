from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

'''
You can't access the register route if you are already logged in. Also in case of invalid forms you need to 
fill the form again and the previous one will be voided. The submission of form is via a POST request which 
successfully redirects you to home page on register
'''
def register_page(request):
    if User.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect('/user/register')
    else: 
        form = UserCreationForm()
        return render(request, "accounts/register.html", {'form': form})


'''
You can't access the Login route if you are already logged in. Also in case of invalid forms you need to 
fill the form again and the previous one will be voided. The submission of form is via a POST request which 
successfully redirects you to home page on Login
'''
def login_page(request):
    if User.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect('/user/login')
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {'form': form})
    

'''
This is served using a button that is added to the navbar at top to Log out the user. Currently 
its a pending task in UI to make the button visible only if the user is logged in otherwise not.
But hey the feature works for now and thats more important
'''
def logout_page(request):
    if request.method == "POST":
        logout(request)
        print("logged out")
        return HttpResponseRedirect("/")


'''
this one is planned to make the user details visibe to him and set up easy access to editing and other activites. 
But sadly for that we need custom user model which i think is not posssible right now so we will leave it for 
sometime later if possible
'''
def profile(request):
    return render(request,'profile.html')

def search_page(request):
    return render(request, 'accounts/search_page.html')
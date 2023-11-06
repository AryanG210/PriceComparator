from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .webscraper import generate_amazon_search, generate_flipkart_search,sorter
from .models import UserData
from django.db.models import Q
from .forms import Register_form

'''
You can't access the register route if you are already logged in. Also in case of invalid forms you need to 
fill the form again and the previous one will be voided. The submission of form is via a POST request which 
successfully redirects you to home page on register
'''
def register_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            if form.clean_pswd() == form.clean_conf_pswd():
                curr_users = UserData.objects.filter(
                    Q(email= form.clean_email())
                )
                if curr_users.all().count() == 0 :
                    user = User.objects.create_user(
                        form.clean_username(),
                        form.clean_email(),
                        form.clean_pswd()
                    )
                    user.first_name = form.clean_name()
                    user.save()
                    Udata = UserData.objects.create(
                        user_id= user,
                        email = user.email,
                        name = user.first_name
                    )
                    Udata.save()

                    user = authenticate(request,username= form.clean_username(), password=form.clean_pswd())
                    if user is not None:
                        login(request,user)
                        return HttpResponseRedirect('/')
                    else:
                        messages.error(request,"Incorrect username/password")
                else:
                    print("Duplicate email")
                    messages.error(request,"Duplicate email")
            else:
                print("The passwords does not match")
                messages.error(request, "The passwords does not match")
        else:
            messages.error(request,'Some error occured. Please try again')

    form = Register_form()
    return render(request, "accounts/register.html", {'form': form})


'''
You can't access the Login route if you are already logged in. Also in case of invalid forms you need to 
fill the form again and the previous one will be voided. The submission of form is via a POST request which 
successfully redirects you to home page on Login
'''
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, "User not found")
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Incorrect username/password")
        else:
            messages.error(request, 'Some error occured. Please Try again')
    
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})
    

'''
This is served using a button that is added to the navbar at top to Log out the user. Currently 
its a pending task in UI to make the button visible only if the user is logged in otherwise not.
But hey the feature works for now and thats more important.
Need to put a modal to confirm logout.
'''
def logout_page(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect("/")


'''
this one is planned to make the user details visibe to him and set up easy access to editing and other activites. 
But sadly for that we need custom user model which i think is not posssible right now so we will leave it for 
sometime later if possible
'''
def profile(request):
    return render(request,'profile.html')

def search_page(request):
    if request.method=='POST':
        search_query = request.POST['Search']
        flipkart_products = generate_flipkart_search(search_query)
        flipkart_products= flipkart_products[:15]
        amazon_products = generate_amazon_search(search_query)
        amazon_products= amazon_products[:15]

        products=amazon_products+flipkart_products
        products=sorter(products)

        return render(request, 'accounts/search_page.html',context={'products':products})
    return render(request, 'accounts/search_page.html',context={'products':[]})
from django.shortcuts import render
from django.contrib.auth.models import User
from Accounts.models import UserData,Images
from django.db.models import Q
from Accounts.webscraper import generate_amazon_search, generate_flipkart_search,sorter
# Create your views here.
def Home(request):
    name = 'user'

    if request.user.is_authenticated:
        user = UserData.objects.filter(
            Q(user_id=request.user.id)  
        ).first()
        if user is not None:
            name =user.name
    images = Images.objects.all()
    context = {'user': name,'images':images} 
    return render(request,'home.html',context)

def Category(request,cat):
    flipkart_products = generate_flipkart_search(cat)
    flipkart_products= flipkart_products[:15]
    amazon_products = generate_amazon_search(cat)
    amazon_products= amazon_products[:15]

    products=amazon_products+flipkart_products
    products=sorter(products)


    return render(request,'category.html',context={'products':products})
    
from django.shortcuts import render
from django.contrib.auth.models import User
from Accounts.models import UserData,Images
from django.db.models import Q
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
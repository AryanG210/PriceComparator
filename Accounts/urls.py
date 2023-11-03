from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.profile),
    path('login/',views.login_page),
    path('register/',views.register_page),
    path('logout/',views.logout_page),
    path('search/',views.search_page)
]

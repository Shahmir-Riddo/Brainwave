from django.contrib import admin
from django.urls import path
from . import views
from brainwapp.models import Profile


urlpatterns = [
    path('', views.index, name="index"),
    path('blogwriter/', views.blogwriter, name="blogwriter"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('productdescwriter/', views.productdescwriter, name="productdescwriter"),
    path('namegenerator/', views.namegenerator, name="namegenerator"),
    path('blogideagenerator/', views.blogideagenerator, name="blogideagenerator"),
    path('paragenerator/', views.paragenerator, name="paragenerator"),
    path('jokegenerator/', views.jokegenerator, name="jokegenerator"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('items/', views.items, name="items")
    
]

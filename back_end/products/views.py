from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializer import ProductSerializer
# Create your views here.
def hello_world(request):
    products = Product.objects.order_by('id')
    context = {'products':products}
    return render(request,'index.html',context)

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
    
        if action == 'signup':
            user = User.objects.create_user(username=username,password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/pro/product1/')
    context = {}
    return render(request, 'login/login.html',context)

@login_required()
def new_product(request):
    context={}
    return render(request,'products/product_new.html',context)

def logout_view(request):
    logout(request)

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

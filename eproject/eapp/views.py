from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
  return render(request,'home.html')

def add_user(request):
  if request.method=='POST':
    f=UserCreationForm(request.POST)
    f.save()
    return redirect('/')
  else:
    f=UserCreationForm()
    context={'form':f}
    return render(request,'form.html',context)
  
  
def login_view(request):
  if request.method=='POST':
    uname=request.POST.get('username')
    passw=request.POST.get('password')
    user=authenticate(request,username=uname,password=passw)
    
    if user is not None:
      request.session['uid']=user.id
      login(request,user)
      return redirect('/')
    else:
      return render(request,'login.html')
  else:
    
    return render(request,'login.html')
  
  
def logout_view(request):
  logout(request)
  return redirect('/')

from .models import Product
def product_list(request):
  pl=Product.objects.all()
  context={'pl':pl}
  return render(request,'plist.html',context)

from .models import cart

def add_to_cart(request,pid):
  product=Product.objects.get(id=pid)
  c=cart()
  c.product=product
  uid=request.session.get('uid')
  user=User.objects.get(id=uid)
  c.user=user
  c.save()
  return redirect('/')


def cart_list(request):
  uid=request.session.get('uid')
  user=User.objects.get(id=uid)
  cl=cart.objects.filter(user=uid)
  context={'cl':cl}
  return render(request,'cartlist.html',context)

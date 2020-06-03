from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['password2']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            
            auth.login(request, new_user)

            return redirect('main:home')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        auth.login(request, user)

        return redirect('/')
    else:
        return render(request,'login.html') 

def logout(request):
    auth.logout(request)
    print('logout 실행')
    return redirect('main:home')

    
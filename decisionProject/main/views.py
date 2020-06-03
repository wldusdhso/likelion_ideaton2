from django.shortcuts import render
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        
    else:
        return render(request, 'register.html')  

    
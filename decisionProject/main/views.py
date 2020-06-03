from django.shortcuts import render, redirect

from vote.models import Question
from django.contrib import auth
# Create your views here.
def home(request):
    hotQuestions = Question.objects.order_by('-total_votes')[:5]
    latestQuestions = Question.objects.order_by('-pub_date')[:5]
    
    return render(request, 'home.html',{
        'hotQuestions' : hotQuestions,
        'latestQuestions' : latestQuestions,
    })

def mypage(request, profile_name):
    return render(request, 'mypage.html')
    

def register(request):
    if request.method=='POST':
        return redirect('/')        
    else:
        return render(request, 'register.html')  

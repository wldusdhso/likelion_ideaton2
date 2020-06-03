from django.shortcuts import render

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

def register(request):
    return render(request, 'register.html')  

   

from django.shortcuts import render, redirect

from vote.models import Question as vQuestion
from question.models import Question, Answer
from django.contrib import auth
# Create your views here.
def home(request):
    hotVotes = vQuestion.objects.order_by('-total_votes')[:5]
    latestVotes = vQuestion.objects.order_by('-pub_date')[:5]
    latestQuestions = Question.objects.order_by('-pub_date')[:5]

    questions = {}
    for q in Question.objects.all() :
        count = Answer.objects.filter(question_id=q.id).count()
        questions[q.id] = count
    hotQuestions = sorted(questions, key = lambda x : questions[x], reverse=True)[:5]

    for i in range(len(hotQuestions)):
        hotQuestions[i] = [Question.objects.get(id=hotQuestions[i]), Answer.objects.filter(question_id=hotQuestions[i]).count()]

    return render(request, 'home.html',{
        'hotQuestions' : hotQuestions,
        'latestQuestions' : latestQuestions,
        'hotVotes' : hotVotes,
        'latestVotes' : latestVotes,
    })

def mypage(request, profile_name):
    return render(request, 'mypage.html')
    

def register(request):
    if request.method=='POST':
        return redirect('/')        
    else:
        return render(request, 'register.html')  

from django.shortcuts import render, redirect
from vote.models import Question as vQuestion
from question.models import Question, Answer
from django.contrib.auth.models import User
from decision.models import Decision
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
    user = User.objects.get(username=profile_name)
    user_decisions = Decision.objects.filter(maker=user)
    return render(request, 'mypage.html', {'user':user, 'decisions': user_decisions})
    

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

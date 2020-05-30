from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .form import QuestionForm
# Create your views here.

def vote_list(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'vote_list.html', {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote.html', {'question': question})

def create(request):
    if request.method =='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('vote_list')
    else :
        form = QuestionForm()
        return render(request, 'create.html', {'form':form})

def add_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('detail', question_id)

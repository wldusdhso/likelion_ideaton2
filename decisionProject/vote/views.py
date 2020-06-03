from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

def vote_list(request):
    question_list = Question.objects.order_by('pub_date')
    return render(request, 'vote_list.html', {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote.html', {'question': question})

def create(request):
    if request.method =='POST':
        new_question = Question()
        new_question.title = request.POST['title']
        new_question.pub_date = timezone.now()
        new_question.writer = request.user
        new_question.save()

        for i in range(int(request.POST['count'])):
            new_choice = Choice()
            text = 'text'+str(i)
            new_choice.question = new_question
            new_choice.text = request.POST[text]
            new_choice.save()
        return redirect('vote:vote_list')
    else :
        return render(request, 'create.html')

def add_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.total_votes += 1
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    question.save()
    return redirect('vote:detail', question_id)

def update(request, question_id):
    if request.method =='POST':
        upd_question = get_object_or_404(Question, pk=question_id)
        upd_question.title = request.POST['title']
        upd_question.pub_date = timezone.now()
        upd_question.writer = request.POST['writer']
        
        choice_set = upd_question.choice_set.all()
        for elem in choice_set:
            elem.delete()

        upd_question.save()

        # print(request.POST['count'])

        for i in range(int(request.POST['count'])):
            new_choice = Choice()
            text = 'text'+str(i)
            new_choice.question = upd_question
            new_choice.text = request.POST[text]
            new_choice.save()

        return redirect('vote:vote_list')
    else :
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'update.html', {'question': question})

def delete(request, question_id):
    del_question = get_object_or_404(Question, pk=question_id)
    del_question.delete()
    return redirect('vote:vote_list')

def delete_choice(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    deleted_choice = question.choice_set.get(pk=choice_id)
    delete_choice.delete()
    question.save()
    return redirect('/')
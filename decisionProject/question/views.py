from django.shortcuts import render
from .models import Question, Answer
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    return render(request,'question/list.html',{'questions':questions})

def new(request):
    return render(request,'question/new.html')

def create(request):
    new_question = Question()
    new_question.title = request.POST['title']
    new_question.writer = request.user.username
    new_question.content = request.POST['content']
    new_question.pub_date = timezone.datetime.now()
    new_question.save()
    return redirect('/question/'+ str(new_question.id))

def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)

    answer = Answer.objects.filter(question_id=question_id)
    print(answer)
    return render(request, 'question/detail.html',{'question':question, 'answer':answer,'edit_answer':edit_answer})

def edit(request,question_id):    
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'question/edit.html',{'question':question})

def update(request,question_id):
    edit_question = get_object_or_404(Question,pk = question_id)
    edit_question.title = request.POST['title']
    edit_question.writer = request.user.username
    edit_question.content = request.POST['content']
    edit_question.pub_date = timezone.datetime.now()
    edit_question.save()
    return redirect('/question/'+ str(edit_question.id))

def delete(request,question_id):
    delete_question = get_object_or_404(Question,pk = question_id)
    delete_question.delete()
    return redirect ('question:list')


def create_answer(request, question_id):
    new_answer = Answer()
    new_answer.writer = request.POST['writer']
    new_answer.content = request.POST['content']
    new_answer.pub_date = timezone.datetime.now()
    new_answer.question_id = question_id
    new_answer.save()

    print('create test')
    return redirect('question:detail',question_id) 
    

def edit_answer(request,answer_id):
    answer = get_object_or_404(Answer,pk = answer_id)
    return render(request, 'question/update_answer.html')

def update_answer(request,answer_id):
    edit_answer = get_object_or_404(Answer,pk = answer_id)
    edit_answer.writer = request.POST['writer']
    edit_answer.content = request.POST['content']
    edit_answer.pub_date = timezone.datetime.now()
    question_id = edit_answer.question_id
    edit_answer.save()
    return redirect('question:detail',question_id) 

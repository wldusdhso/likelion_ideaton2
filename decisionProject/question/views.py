from django.shortcuts import render
from .models import Question
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
# Create your views here.

def list(request):
    questions = Question.objects.all()
    return render(request,'list.html',{'questions':questions})

def new(request):
    return render(request,'new.html')

def create(request):
    new_question = Question()
    new_question.title = request.POST['title']
    new_question.content = request.POST['content']
    new_question.pub_date = timezone.datetime.now()
    new_question.save()
    return redirect('/question/question/'+ str(new_question.id))

def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'detail.html',{'question':question})

def edit(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'edit.html',{'question':question})

def update(request,question_id):
    edit_question = get_object_or_404(Question,pk = question_id)
    edit_question.title = request.POST['title']
    edit_question.content = request.POST['content']
    edit_question.pub_date = timezone.datetime.now()
    edit_question.save()
    return redirect('/question/question/'+ str(edit_question.id))

def delete(request,question_id):
    delete_question = get_object_or_404(Question,pk = question_id)
    delete_question.delete()
    return redirect ('list')

def answer(request):
    answer = Answer.objects.all()
    return render(request, {'answer':answer})

#answer 함수는 어떻게 해야할까..
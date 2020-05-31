from django.shortcuts import render
from .models import Question, Answer
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
    new_question.writer = request.POST['writer']
    new_question.content = request.POST['content']
    new_question.pub_date = timezone.datetime.now()
    new_question.save()
    return redirect('/question/'+ str(new_question.id))

def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)

    answer = Answer.objects.filter(question_id=question_id)
    print(answer)
    return render(request, 'detail.html',{'question':question, 'answer':answer})

def edit(request,question_id):    
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'edit.html',{'question':question})

def update(request,question_id):
    edit_question = get_object_or_404(Question,pk = question_id)
    edit_question.title = request.POST['title']
    edit_question.writer = request.POST['writer']
    edit_question.content = request.POST['content']
    edit_question.pub_date = timezone.datetime.now()
    edit_question.save()
    return redirect('/question/'+ str(edit_question.id))

def delete(request,question_id):
    delete_question = get_object_or_404(Question,pk = question_id)
    delete_question.delete()
    return redirect ('list')


# def create_answer(request):
#     return redirect('detail/'+ )


def create_answer(request, question_id):
    new_answer = Answer()
    new_answer.writer = request.POST['writer']
    new_answer.content = request.POST['content']
    new_answer.pub_date = timezone.datetime.now()
    new_answer.question_id = question_id
    new_answer.save()

    print('create test')
    return redirect('detail',question_id) 
    
# detail_answer = Answer()
#     detail_answer.writer = request.POST['writer']
#     detail_answer.content = request.POST['content']
#     detail_answer.pub_date = timezone.datetime.now()
#     detail_answer.save()
#     return redirect('detail')

# def create(request, question_id):
#     detail_answer = Answer()
#     detail_answer.writer = request.POST['writer']
#     detail_answer.content = request.POST['content']
#     detail_answer.pub_date = timezone.datetime.now()
#     detail_answer.save()
#     return redirect('detail')
def answer_edit(request,question_id):    
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'answer_edit.html',{'question':question})


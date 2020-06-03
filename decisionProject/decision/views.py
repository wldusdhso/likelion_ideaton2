from django.shortcuts import render, get_object_or_404, redirect
from .models import Decision
from django.shortcuts import render
import random


# Create your views here.


def list(request):    
    if request.user.is_authenticated:
        # decisions = get_object_or_404(Decision, maker=request.user)
        decisions = Decision.objects.filter(maker=request.user)
        return render(request, 'decision/list.html', {'decisions': decisions})
    else:
        return redirect('main:login')


def result(request):
    if request.method=='POST':
        content = request.POST['content']
        number = random.randrange(0,2)

        if number == 0:
            choice = False
        else:
            choice = True 

        new_decision = Decision()
        new_decision.choice_content = content
        new_decision.maker = request.user
        new_decision.result = choice
        new_decision.save()
        
    return render(request, 'decision/result.html', {'decision' : new_decision})


def delete(request, decision_id):
    delete_decision = get_object_or_404(Decision, pk=decision_id)
    delete_decision.delete()
    
    return redirect('decision:list')
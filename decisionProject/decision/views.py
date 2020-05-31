from django.shortcuts import render, get_object_or_404, redirect
from .models import Decision
from .form import DecisionForm
from django.shortcuts import render
import random

# Create your views here.

def list(request):
    if request.method == 'POST':
        form = DecisionForm(request.POST, request.FILES) #입력값
        if form.is_valid():
            content = form.save(commit = False) #임시저장
            content.save() #저장
            return render(request, 'result.html')
    else:
        form = DecisionForm()
        return render(request, 'list.html', {'form':form})


def result(request):
    number = random.randrange(0,2)

    if number == 0:
        choice = "NO"
    else:
        choice ="YES" 
    return render(request, 'result.html', {'choice':choice})


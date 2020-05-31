from django.shortcuts import render


# Create your views here.

def decision(request):
    return render(request, 'decision.html')


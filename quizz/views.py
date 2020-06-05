from django.shortcuts import render

# Create your views here.

def detail(request, idQuizz):
    return render(request, 'quizz_detail.html', {})
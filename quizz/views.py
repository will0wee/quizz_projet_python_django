from django.shortcuts import render

# Create your views here.

def detail(request, idQuizz):
    return render(request, 'quizz_detail.html', {'idQuizz': idQuizz})

def instancesQuizz(request, idQuizz):
    banner = [
        {'libellé': "titre", 'url': "hompage.html"},
        {'libellé': "titre", 'url': "hompage.html"}
    ]
    return render(request, 'listeInstanceQuizz.html', {'idQuizz': idQuizz, 'banner': banner})
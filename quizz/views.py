from django.shortcuts import render, redirect

# Create your views here.

def detail(request, idQuizz):
    if request.session['userId'] is None:
        redirect('login')
    if True:
        banner = [
            {'libelle': "Home", 'url': "home"},
            {'libelle': "Liste des instance de quizz", 'url': "liste_instance_quizz", 'id': 1}
        ]
    else:
        banner = [
            {'libelle': "Home", 'url': "home"}
        ]
    return render(request, 'quizz_detail.html', {'idQuizz': idQuizz, 'banner': banner, 'currentElement': 'Détail du quizz'})

def instancesQuizz(request, idQuizz):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'listeInstanceQuizz.html', {'idQuizz': idQuizz, 'banner': banner, 'currentElement': 'Liste des instance de quizz'})
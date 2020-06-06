from django.shortcuts import render

# Create your views here.

def detail(request, idQuizz):
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
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'listeInstanceQuizz.html', {'idQuizz': idQuizz, 'banner': banner, 'currentElement': 'Liste des instance de quizz'})

def add(request):
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'add_quizz.html', { 'banner': banner, 'currentElement': 'Ajout d un quizz'})

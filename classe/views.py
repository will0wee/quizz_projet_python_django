from django.shortcuts import render, redirect

def classroom(request):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'classroom.html', {'navigation': 'active', 'banner': banner, 'currentElement': 'Liste des instance de quizz'})

def details_classroom(request, idClasse = 0):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"},
        {'libelle': "Liste des classes", 'url': "listeClassRoom"},
    ]
    return render(request, 'details_classroom.html',  {'navigation': 'active', 'idClasse': idClasse, 'banner': banner, 'currentElement': 'Liste des élèves'})
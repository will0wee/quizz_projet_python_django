from django.shortcuts import render

def classroom(request):
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'classroom.html', {'navigation': 'active', 'banner': banner, 'currentElement': 'Liste des instance de quizz'})

def details_classroom(request, idClasse = 0):
    banner = [
        {'libelle': "Home", 'url': "home"},
        {'libelle': "Liste des classes", 'url': "listeClassRoom"},
    ]
    return render(request, 'details_classroom.html',  {'navigation': 'active', 'idClasse': idClasse, 'banner': banner, 'currentElement': 'Liste des élèves'})
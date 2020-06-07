from django.shortcuts import render, redirect
from .forms import QuizzForm
from .models import Quizz
from .forms import QuestionForm
from .models import Question
from django.http import HttpResponse
from django.contrib.auth.models import User

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

def add(request, idQuizz = None):
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    form = QuizzForm(request.POST or None)
    if form.is_valid() and 'submitQuizz' in request.POST:
        monQuizz = Quizz(libelle = form.cleaned_data['libelle'], professeur = User.objects.filter(id=request.session.get("userId"))[0])
        monQuizz.save()
        idQuizz = Quizz.objects.latest("id")
        return redirect('add_quizz', idQuizz)
    currentElement = "ajout d'un quizz"
    quizzs = Quizz.objects.raw("SELECT * from quizz_quizz")


    formQuestion = QuestionForm(request.POST or None)

    if formQuestion.is_valid() and 'submitQuestion' in request.POST and idQuizz is not None :
        maQuestion = Question(libelle = form.cleaned_data['libelle'], quizz = Quizz.objects.filter(id=idQuizz)[0])
        maQuestion.save()
    else:
        if request.method == 'POST':
            return HttpResponse("EUH SA MARCHE PO")
    questions = Question.objects.raw("SELECT * from quizz_question")


    return render(request, 'add_quizz.html', locals())

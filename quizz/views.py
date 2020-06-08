from django.shortcuts import render, redirect
from .models import Quizz, DemandeQuizz, Instance_quizz, Question, Reponse_possible, Reponse
from classe.models import Classe, Liste_classe
from user.models import User_data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import QuestionForm, ReponseForm, QuizzForm
from django.http import HttpResponse
import logging
import datetime

# Create your views here.

def detail(request, idQuizz):
    if request.session['userId'] is None:
        redirect('login')
    if request.session.get('userType') == 2:
        banner = [
            {'libelle': "Home", 'url': "home"},
            {'libelle': "Liste des instance de quizz", 'url': "liste_instance_quizz", 'id': 1}
        ]
    else:
        banner = [
            {'libelle': "Home", 'url': "home"}
        ]
    return render(request, 'quizz_detail.html', {'idQuizz': idQuizz,
                                                 'banner': banner,
                                                 'currentElement': 'Détail du quizz',
                                                 'user': {'userFirstName': request.session.get('userFirstName'),
                                                         'userLastName': request.session.get('userLastName'),
                                                         'userTypeLibelle': request.session.get('userTypeLibelle')
                                                         }})

def instancesQuizz(request, idQuizz):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    return render(request, 'listeInstanceQuizz.html', {'idQuizz': idQuizz,
                                                       'banner': banner,
                                                       'currentElement': 'Liste des instance de quizz',
                                                       'user': {'userFirstName': request.session.get('userFirstName'),
                                                                'userLastName': request.session.get('userLastName'),
                                                                'userTypeLibelle': request.session.get(
                                                                    'userTypeLibelle')
                                                                }})
@csrf_protect
def homeQuizz(request):
    logger = logging.getLogger('app_api')
    banner = [
        {'libelle': "Home", 'url': "home"},
    ]
    if request.session.get('userType') == 1:
        templates = 'homeQuizzEleve.html'
        data = {'lstQuizz': DemandeQuizz.objects.filter(eleve=request.session.get('userId')).select_related('eleve', 'quizz')}
    else:
        templates = 'homeQuizzProfesseur.html'
        data = {'lstQuizz': Quizz.objects.raw("SELECT quizz_quizz.id, quizz_quizz.libelle, (SELECT COUNT(id) FROM quizz_demandequizz WHERE quizz_demandequizz.quizz_id = quizz_quizz.id) as nbAttente, (SELECT COUNT(id) FROM quizz_instance_quizz WHERE quizz_instance_quizz.quizz_id = quizz_quizz.id) as nbTermine FROM quizz_quizz"),
                'classes': Classe.objects.filter(professeur=request.session.get('userId')),
                'eleves': User_data.objects.filter(user_type=1).select_related('user')}
        if request.method == 'POST':
            classe = request.POST.classe
            users = Liste_classe.objects.filter(classe__in=classe).select_related('user')
            for element in users:
                demande = DemandeQuizz(quizz=Quizz.objects.filter(id=request.POST.idQuizz),
                                       eleve=User.objects.filter(id=element.eleve.id))
                demande.save()
            eleve = request.POST.eleve
            for element in eleve:
                demande = DemandeQuizz(quizz=Quizz.objects.filter(id=request.POST.idQuizz),
                                       eleve=User.objects.filter(id=element))
                demande.save()
    return render(request, templates, {'banner': banner,
                                        'currentElement': 'Liste des quizzs',
                                        'data': data,
                                        'user': {'userFirstName': request.session.get('userFirstName'),
                                            'userLastName': request.session.get('userLastName'),
                                            'userTypeLibelle': request.session.get(
                                                'userTypeLibelle')
                                            }})

def deleteQuizz(request, idQuizz):
    Quizz.objects.filter(id=idQuizz).delete()
    return redirect('homeQuizz')

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

def create_quizz(request, idQuizz):
    logger = logging.getLogger('app_api')
    if DemandeQuizz.objects.filter(quizz=Quizz.objects.filter(id=idQuizz)[0],
                                   eleve=User.objects.filter(id=request.session.get('userId'))[0]).exists():
        DemandeQuizz.objects.filter(quizz=Quizz.objects.filter(id=idQuizz)[0],
                                      eleve=User.objects.filter(id=request.session.get('userId'))[0]).delete()
        newQuizz = Instance_quizz(eleve=User.objects.filter(id=request.session.get('userId'))[0],
                                  quizz=Quizz.objects.filter(id=idQuizz)[0])
        newQuizz.date = datetime.datetime.today().strftime('%Y-%m-%d')
        newQuizz.libelle = Quizz.objects.filter(id=idQuizz)[0].libelle+' par '+User.objects.filter(id=request.session.get('userId'))[0].first_name+' '+User.objects.filter(id=request.session.get('userId'))[0].first_name+' le '+datetime.datetime.today().strftime('%d %B')
        test = newQuizz.save()
        logger.error(test)
        return redirect('faire_quizz', idQuizz)
    else:
        return redirect('homeQuizz')

def faire_quizz(request, idQuizz, question = 1):
    if request.session.get('userId', 0) == 0:
        return redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    currentElement = 'Répondre à un quizz'
    user = {'userFirstName': request.session.get('userFirstName'),
            'userLastName': request.session.get('userLastName'),
            'userTypeLibelle': request.session.get(
                'userTypeLibelle')}

    previousQuestion = question-1
    nextQuestion = question+1
    lstQuestion = Question.objects.filter(quizz=Quizz.objects.filter(id=idQuizz)[0])
    sizeQuestion = len(lstQuestion)
    if question > sizeQuestion:
        return redirect('home')
    currentQuestion = lstQuestion[(question-1)]
    form = ReponseForm(request.POST or None)
    form.fields["reponse"].queryset = Reponse_possible.objects.filter(question=currentQuestion)
    if form.is_valid():
        myReponse = Reponse(question=currentQuestion,
                instance_quizz=Instance_quizz.objects.filter(quizz=Quizz.objects.filter(id=idQuizz)[0], eleve=User.objects.filter(id=request.session.get('userId'))[0])[0],
                reponse=form.cleaned_data['reponse'])
        myReponse.save()
        return redirect('faire_quizz', idQuizz, nextQuestion)
    return render(request, 'doQuizz.html', locals())
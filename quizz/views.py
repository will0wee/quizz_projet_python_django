from django.shortcuts import render, redirect
from .models import Quizz, DemandeQuizz, Instance_quizz
from classe.models import Classe, Liste_classe
from user.models import User_data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

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
    banner = [
        {'libelle': "Home", 'url': "home"},
    ]
    if request.session.get('') == 1 or True:
        templates = 'homeQuizzEleve.html'
        data = {'lstQuizz': DemandeQuizz.objects.filter(eleve=request.session.get('userId'))}

    else:
        templates = 'homeQuizzProfesseur.html'
        data = {'lstQuizz': Quizz.objects.raw("SELECT quizz_quizz.id, quizz_quizz.libelle, (SELECT COUNT(id) FROM quizz_demandequizz WHERE quizz_demandequizz.quizz_id = quizz_quizz.id) - (SELECT COUNT(id) FROM quizz_instance_quizz WHERE quizz_instance_quizz.quizz_id = quizz_quizz.id) as nbAttente, (SELECT COUNT(id) FROM quizz_instance_quizz WHERE quizz_instance_quizz.quizz_id = quizz_quizz.id) as nbTermine FROM quizz_quizz"),
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
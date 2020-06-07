from django.shortcuts import render, redirect
from .forms import ClassForm, addEleveForm
from .models import Classe, Liste_classe
from django.contrib.auth.models import User
from user.models import User_data
from django.views.decorators.csrf import csrf_protect

def classroom(request, classroomId = None):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    navigation= 'active'
    currentElement= 'Liste des classes'
    user= {'userFirstName': request.session.get('userFirstName'),
         'userLastName': request.session.get('userLastName'),
         'userTypeLibelle': request.session.get('userTypeLibelle')
         }
    if classroomId is None:
        initial={}
        libelleBtn = 'Ajouter'
    else:
        initial={'libelle': Classe.objects.filter(id=classroomId)[0].libelle}
        libelleBtn = 'Modifier'
    form = ClassForm(request.POST or None, initial=initial)
    if form.is_valid():
        classe = Classe(libelle=form.cleaned_data['libelle'], professeur=User.objects.filter(id=request.session.get('userId'))[0])
        if classroomId is not None:
            classe.id = classroomId
        classe.save()

    listClassroom = Classe.objects.raw("SELECT libelle, id, (SELECT COUNT(id) FROM classe_liste_classe WHERE classe_id = classe_classe.id) as count FROM classe_classe WHERE professeur_id="+str(request.session.get('userId')))

    return render(request, 'classroom.html', locals())

@csrf_protect
def details_classroom(request, classroomId = 0):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"},
        {'libelle': "Liste des classes", 'url': "listeClassRoom"},
    ]
    currentElement = 'Liste des élèves'
    user = {'userFirstName': request.session.get('userFirstName'),
             'userLastName': request.session.get('userLastName'),
             'userTypeLibelle': request.session.get('userTypeLibelle')
             }
    navigation = 'active'

    classroom = Classe.objects.filter(id=classroomId)[0]
    classroomData = Liste_classe.objects.filter(classe=classroomId)
    classroomEleve = []
    for element in classroomData:
        classroomEleve.append(element.eleve.id)
    eleveDispo = User_data.objects.filter(user_type=1).exclude(user__in=classroomEleve).select_related('user')

    return render(request, 'details_classroom.html', locals())

def delete_classroom(request, classroomId):
    Classe.objects.filter(id=classroomId).delete()
    return redirect('listeClassRoom')

def delete_student(request, classroomId, eleveId):
    Liste_classe.objects.filter(eleve=eleveId, classe=classroomId).delete()
    return redirect(details_classroom, classroomId)

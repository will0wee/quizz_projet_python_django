from django.shortcuts import render, redirect
from .authenticator import Authenticator
from .forms import LoginForm, UserForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from quizz.models import DemandeQuizz, Instance_quizz, Reponse, Reponse_possible, Quizz
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.session.get("userId", 0) == 0:
        return redirect("login")
    if request.session.get("userType", 1) == 1:
        lstDemande = DemandeQuizz.objects.filter(eleve=User.objects.filter(id=request.session.get("userId"))[0]).select_related('quizz')
        lstInstance = Instance_quizz.objects.filter(eleve=User.objects.filter(id=request.session.get("userId"))[0]).select_related('quizz')
        lstResult = []
        for element in lstInstance:
            max = len(Reponse.objects.filter(instance_quizz=element))
            if max == 0:
                note = '-'
            else:
                note = len(Reponse.objects.select_related('reponse').filter(reponse__valeur=1, instance_quizz=element)) * 20 / max
            data = {'note': note,
                    'instance': element}
            lstResult.append(data)
        data = {'lstDemande': lstDemande, 'lstInstance': lstInstance, 'lstResult': lstResult}
    else:
        quizzs = Quizz.objects.filter(professeur=User.objects.filter(id=request.session.get("userId"))[0])
        data = []
        for quizz in quizzs:
            lstInstance = Instance_quizz.objects.filter(quizz=quizz)
            noteInstance = []
            for element in lstInstance:
                max = len(Reponse.objects.filter(instance_quizz=element))
                if max != 0:
                    noteInstance.append(len(Reponse.objects.select_related('reponse').filter(reponse__valeur=1,
                                                                                instance_quizz=element)) * 20 / max)
            if len(noteInstance) != 0:
                note = sum(noteInstance) / len(noteInstance)
            else:
                note = '-'
            data.append({'quizz': quizz, 'note': note})



    return render(request, 'home.html', {'currentElement': 'Acceuil',
                                         'user': {'userFirstName': request.session.get('userFirstName'),
                                                  'userLastName': request.session.get('userLastName'),
                                                  'userTypeLibelle': request.session.get('userTypeLibelle', 'test'),
                                                  'userType': request.session.get('userType', 1)
                                                  },
                                         'type': type,
                                         'data': data
                                         })


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        auth = Authenticator()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        if(auth.authenticate(request, username, password)):
            return redirect('home')
        else:
            msg = "Mauvais nom d'utilisateur/mot de passe"
    else:
        if request.method == 'POST':
            msg = "Veuillez remplir tous les champs correctements"
    return render(request, 'login.html', locals())

def profile(request):
    if request.session['userId'] is None:
        redirect('login')
    banner = [
        {'libelle': "Home", 'url': "home"}
    ]
    currentElement = 'Détail du compte'
    navigation = 'active'

    form = UserForm(request.POST or None, initial = {'first_name': request.session.get('userFirstName'),
                         'last_name': request.session.get('userLastName'),
                         'username': request.session.get('userUsername'),
                         'email': request.session.get('userEmail')})

    if form.is_valid():
        currentUser = User.objects.filter(id=request.session.get('userId'))[0]
        if User.objects.filter(username=form.cleaned_data['username'], email=form.cleaned_data['email']).exclude(id=request.session.get('userId')).exists():
            msg = 'Utilisateur avec le même username ou email'
        else:
            try:
                currentUser.first_name = form.cleaned_data['first_name']
                currentUser.last_name = form.cleaned_data['last_name']
                currentUser.username = form.cleaned_data['username']
                currentUser.email = form.cleaned_data['email']
                currentUser.save()
                request.session['userFirstName'] = form.cleaned_data['first_name']
                request.session['userLastName'] = form.cleaned_data['last_name']
                request.session['userUsername'] = form.cleaned_data['username']
                request.session['userEmail'] = form.cleaned_data['email']
            except IntegrityError:
                msg = 'Utilisateur avec le même username ou email'


    user = {'userFirstName': request.session.get('userFirstName'),
            'userLastName': request.session.get('userLastName'),
            'userEmail': request.session.get('userEmail'),
            'userTypeLibelle': request.session.get('userTypeLibelle'), }
    return render(request, 'profile.html', locals())

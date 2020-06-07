from django.shortcuts import render, redirect
from .authenticator import Authenticator
from .forms import LoginForm, UserForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.session['userId'] is None:
        redirect('login')
    return render(request, 'home.html', {'currentElement': 'Acceuil', 'user': {'userFirstName': request.session.get('userFirstName'), 'userLastName': request.session.get('userLastName'), 'userTypeLibelle': request.session.get('userTypeLibelle', 'test')}})

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

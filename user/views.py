from django.shortcuts import render, redirect
from .authenticator import Authenticator
from .forms import LoginForm

# Create your views here.
def home(request):
    if request.session['userId'] is None:
        redirect('login')
    return render(request, 'home.html', {'Banner' : "HomePage", 'BannerHref' : ""})

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
    return render(request, 'profile.html', {'navigation': 'active', 'banner': banner, 'currentElement': 'Détail du compte'})


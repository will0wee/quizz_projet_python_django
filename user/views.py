from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def home(request):
    ## Si user pas connecté alors retourner login
    return render(request, 'home.html', {'Banner' : "HomePage", 'BannerHref' : ""})

def logon(request, username):
    return render(request, 'logon.html', {'username': username})

def login2(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        #login()
        redirect('home')

    return render(request, 'login2.html', {})

def login(request):
    return render(request, 'login.html', {})

def modele(request):
    return render(request, 'modele.html', {'content' : render_to_response()})
    
def profile(request):
    return render(request, 'profile.html', {})


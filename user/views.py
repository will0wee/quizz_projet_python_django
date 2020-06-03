from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    ## Si user pas connecté alors retourner login
    return render(request, 'home.html', {'Banner' : "HomePage", 'BannerHref' : ""})

def login(request):
    return HttpResponse("""<h3>Login</h3>""")

def logon(request, username):
    return render(request, 'logon.html', {'username': username})

def login(request):
    return render(request, 'login.html', {})

def modele(request):
    return render(request, 'modele.html', {'content' : render_to_response()})
    
def profile(request):
    return render(request, 'profile.html', {})


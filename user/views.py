from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""<h1>Home sweet home</h1>""")

def login(request):
    return HttpResponse("""<h3>Login</h3>""")
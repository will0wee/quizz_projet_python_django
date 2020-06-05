from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('logon/<username>', views.logon),
    path('modele/', views.modele),
<<<<<<< HEAD
    path('login2/', views.login2, name='login2'),
=======
    path('profile/', views.profile, name="profilUtilisateur"),
>>>>>>> c5c7acfe89addf1ed5f6e6ec154a06519b656201
]

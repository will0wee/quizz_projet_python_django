from django.urls import path, include
from . import views

urlpatterns = [
    path('logon/<username>', views.logon),
    path('modele/', views.modele),
    path('login2/', views.login2, name='login2'),
    path('profile/', views.profile, name="profilUtilisateur"),
]

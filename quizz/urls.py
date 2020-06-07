from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:idQuizz>', views.detail, name='quizz_detail'),
    path('instancesQuizz/<int:idQuizz>', views.instancesQuizz, name='liste_instance_quizz'),
    path('', views.homeQuizz, name='homeQuizz'),
    path('delete/<int:idQuizz>', views.deleteQuizz, name='deleteQuizz'),
    path('add/', views.add, name='add_quizz'),
    path('add/<int:idQuizz>', views.add, name='add_quizz')
]
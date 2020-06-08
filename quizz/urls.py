from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:idQuizz>', views.detail, name='quizz_detail'),
    path('instancesQuizz/<int:idQuizz>', views.instancesQuizz, name='liste_instance_quizz'),
    path('', views.homeQuizz, name='homeQuizz'),
    path('delete/<int:idQuizz>', views.deleteQuizz, name='deleteQuizz'),
    path('add/', views.add, name='add_quizz'),
    path('add/<int:idQuizz>', views.add, name='add_quizz'),
    path('create_quizz/<int:idQuizz>', views.create_quizz, name='create_quizz'),
    path('faire_quizz/<int:idQuizz>', views.faire_quizz, name='faire_quizz'),
    path('faire_quizz/<int:idQuizz>/<int:question>', views.faire_quizz, name='faire_quizz')
]
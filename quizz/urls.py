from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:idQuizz>', views.detail, name='quizz_detail'),

]
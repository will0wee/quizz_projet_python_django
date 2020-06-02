from django.db import models
from user.models import User


class Quizz(models.Model):
    professeur = models.ForeignKey(User, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

class Instance_quizz(models.Model):
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    date = models.DateField(auto_now = True)
    libelle = models.CharField(max_length=255)

class Question(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

class Reponse_possible(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)
    libelle = models.BooleanField()

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    instance_quizz = models.ForeignKey(Instance_quizz, on_delete=models.CASCADE)
    reponse = models.ForeignKey(Reponse_possible, on_delete=models.CASCADE)


# Create your models here.

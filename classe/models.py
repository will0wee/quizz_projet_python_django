from django.db import models
from user.models import User


class Classe(models.Model):
    professeur = models.ForeignKey(User, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

class Liste_classe(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Classe(models.Model):
    professeur = models.ForeignKey(User, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Classe"
        ordering = ['professeur', 'libelle']

    def __str__(self):
        return self.libelle

class Liste_classe(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Contenu des classe"
        ordering = ['classe', 'eleve']
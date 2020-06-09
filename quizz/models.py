from django.db import models
from django.contrib.auth.models import User

class Quizz(models.Model):
    professeur = models.ForeignKey(User, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Quizz"
        ordering = ['professeur', 'libelle']

    def __str__(self):
        return self.libelle

class Instance_quizz(models.Model):
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    date = models.DateField(auto_now = True)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Instance des quizz"
        ordering = ['quizz', 'date', 'eleve']

    def __str__(self):
        return self.libelle

class Question(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Question"
        ordering = ['quizz', 'libelle']

    def __str__(self):
        return self.libelle

class Reponse_possible(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)
    valeur = models.BooleanField()

    class Meta:
        verbose_name = "Réponse possible"
        ordering = ['question', 'valeur']

    def __str__(self):
        return self.libelle

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    instance_quizz = models.ForeignKey(Instance_quizz, on_delete=models.CASCADE)
    reponse = models.ForeignKey(Reponse_possible, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Réponse"
        ordering = ['instance_quizz', 'question']

    def __str__(self):
        return self.reponse

class DemandeQuizz(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Demande de quizz"
        ordering = ['quizz', 'eleve']


# Create your models here.

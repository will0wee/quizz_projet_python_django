from django.db import models
from django.contrib.auth.models import User

class User_type(models.Model):
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "type d'utilisateur"

    def __str__(self):
        return self.libelle

class User_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(User_type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Donneés supplémentaire de l'utilisateur (type)"
        ordering = ['user', 'user_type']
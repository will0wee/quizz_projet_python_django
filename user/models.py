from django.db import models
from django.utils import timezone

# Create your models here.
class User_type(models.Model):
    libelle = models.CharField(max_length=255)

class User(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    id_user_type = models.ForeignKey(User_type,  on_delete=models.CASCADE)


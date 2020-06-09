from django.contrib import admin
from .models import Quizz, Instance_quizz, Question, Reponse_possible, Reponse, DemandeQuizz

class QuizzAdmin(admin.ModelAdmin):
    list_display = ('professeur', 'libelle')
    list_filter = ('professeur',)
    ordering = ('professeur', 'libelle')
    search_fields = ('professeur', 'libelle')

class Instance_quizzAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'quizz', 'libelle', 'date')
    list_filter = ('eleve', 'quizz', 'date',)
    date_hierarchy = 'date'
    ordering = ('quizz', 'eleve', 'libelle')
    search_fields = ('quizz', 'eleve', 'libelle')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quizz', 'libelle')
    list_filter = ('quizz',)
    ordering = ('quizz', 'libelle')
    search_fields = ('quizz', 'libelle')

class Reponse_possibleAdmin(admin.ModelAdmin):
    list_display = ('question', 'libelle', 'valeur')
    list_filter = ('question',)
    ordering = ('question', 'valeur', 'libelle')
    search_fields = ('question', 'libelle')

class ReponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse')
    list_filter = ('question',)
    ordering = ('question', 'reponse')
    search_fields = ('question', 'reponse')

class DemandeQuizzAdmin(admin.ModelAdmin):
    list_display = ('quizz', 'eleve')
    list_filter = ('quizz', 'eleve')
    ordering = ('quizz', 'eleve')
    search_fields = ('quizz', 'eleve')

admin.site.register(Quizz, QuizzAdmin)
admin.site.register(Instance_quizz, Instance_quizzAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse_possible, Reponse_possibleAdmin)
admin.site.register(Reponse, ReponseAdmin)
admin.site.register(DemandeQuizz, DemandeQuizzAdmin)
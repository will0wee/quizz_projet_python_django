from django.contrib import admin
from .models import Classe, Liste_classe

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('professeur', 'libelle')
    list_filter = ('professeur',)
    ordering = ('professeur', 'libelle')
    search_fields = ('professeur', 'libelle')

class Liste_classeAdmin(admin.ModelAdmin):
    list_display = ('classe', 'eleve')
    list_filter = ('classe', 'eleve',)
    ordering = ('classe', 'eleve')
    search_fields = ('classe', 'eleve')

admin.site.register(Classe, ClasseAdmin)
admin.site.register(Liste_classe, Liste_classeAdmin)

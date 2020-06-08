from django import forms
from .models import Quizz, Reponse
from .models import Question
import logging

class QuizzForm(forms.ModelForm):
    class Meta:
            model = Quizz
            fields = ['libelle',]

class QuestionForm(forms.ModelForm):
    class Meta:
            model = Question
            fields = ['libelle']

class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['reponse', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reponse'].widget.attrs.update({'class': 'form-control'})



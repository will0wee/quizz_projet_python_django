from django import forms
from .models import Quizz
from .models import Question

class QuizzForm(forms.ModelForm):
    class Meta:
            model = Quizz
            fields = ['libelle',]

class QuestionForm(forms.ModelForm):
    class Meta:
            model = Question
            fields = ['libelle']


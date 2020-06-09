from django import forms
from .models import Quizz
from .models import Question
from .models import Reponse_possible

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
            model = Reponse_possible
            fields = ['libelle','valeur','question']


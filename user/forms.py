from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100, label="Votre adresse e-mail")
    passqord = forms.CharField(max_length=100, label="Votre mot de passe")
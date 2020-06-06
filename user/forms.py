from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100,
                                label="Votre adresse e-mail",
                                widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=100,
                               label="Votre mot de passe",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
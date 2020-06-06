from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                                label="Votre adresse e-mail",
                                widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=100,
                               label="Votre mot de passe",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                               label="Prénom",
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=150,
                               label="Nom",
                               widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    username = forms.CharField(max_length=150,
                                label="Nom d'utilisateur",
                                widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(max_length=254,
                               label="email",
                               widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Importa ambos aquí
from .models import Perfil

# FORMULARIO 1: Para crear el usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# FORMULARIO 2: Para editar el usuario (el que ya tienes)
class UserEditForm(UserChangeForm):
    password = None 
    email = forms.EmailField(label="Correo Electrónico")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    avatar = forms.ImageField(label="Foto de Perfil", required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
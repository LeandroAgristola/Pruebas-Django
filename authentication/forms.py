from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm

# Validador personalizado para campos que solo deben aceptar letras
def validar_solo_letras(value):
    if not value.isalpha():
        raise ValidationError('Este campo solo debe contener letras.')

# Validador personalizado para teléfono (solo números)
def validar_solo_numeros(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError('El teléfono solo debe contener números.')

class RegistroFormulario(UserCreationForm):
    nombre = forms.CharField(
        max_length=100,
        validators=[validar_solo_letras],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Juan'
        })
    )
    apellido = forms.CharField(
        max_length=100,
        validators=[validar_solo_letras],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Perez'
        })
    )
    telefono = forms.CharField(
        max_length=20,
        validators=[validar_solo_numeros],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '0115345456'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@email.com'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar Contraseña'
        })
    )

    class Meta:
        model = UserCreationForm.Meta.model  # Usar el mismo modelo que UserCreationForm
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email', 'password1', 'password2')
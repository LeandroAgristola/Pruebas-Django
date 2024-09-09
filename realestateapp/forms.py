from django import forms
from django.core.exceptions import ValidationError
import re

# Validador personalizado para campos que solo deben aceptar letras
def validar_solo_letras(value):
    if not value.isalpha():
        raise ValidationError('Este campo solo debe contener letras.')

# Validador personalizado para teléfono (solo números)
def validar_solo_numeros(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError('El teléfono solo debe contener números.')

class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        validators=[validar_solo_letras],  # Validación para solo letras
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Juan'
        })
    )
    apellido = forms.CharField(
        max_length=100, 
        validators=[validar_solo_letras],  # Validación para solo letras
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Perez'
        })
    )
    telefono = forms.CharField(
        max_length=20,
        validators=[validar_solo_numeros],  # Validación para solo números
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
    consulta = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Escribe tu consulta aquí'
        })
    )

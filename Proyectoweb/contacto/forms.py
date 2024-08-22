from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True,max_length=50)
    email=forms.EmailField(label="email",required=True,max_length=50)
    contenido=forms.CharField(label="contenido",required=False,max_length=150,widget=forms.Textarea)


#Requerimiento es registrar un nuevo departamento, pero con un empleado a cargo.

from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField( max_length=50)
    apellido = forms.CharField( max_length=50)
    departamento = forms.CharField( max_length=50)
    shorname = forms.CharField( max_length=20)
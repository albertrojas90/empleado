from django import forms 
from .models import Prueba

class PruebaForm(forms.ModelForm):    
    class Meta:
        model= Prueba
         #fields = ('__all__') si se quiere mostrar todos los campos de una vez
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
         )
        # para personalizar el formulario usamos widgets. se le conoce como diccionario
        widgets= {
            'titulo': forms.TextInput(
                attrs ={
                       'placeholder':'Ingrese texto aquí' 
                }
            )
        }
        #si se quieren cantidad mayor a un nro, se puede hacer la validación
    def clean_cantidad(self): 
        cantidad = self.cleaned_data['cantidad']# recupera el valor que se tiene dentro de cantidad
        if cantidad < 10:
            raise forms.ValidationError(' Ingrese un número mayor a 10 ')
        return cantidad
from django.shortcuts import render
#vista generica preparada por django
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
#realizamos la conexión del forms.py con el views.py hacendo la importación, luego se vincula a la vista
from .forms import PruebaForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A','B','C'] 
    #para hacer la conexión dl views.py/home y traerme el valor del array
    context_object_name = 'lista_prueba' 

 

class MODELPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lita_prueba'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    #método alterno es usando el form
    form_class = PruebaForm
    success_url = '/'

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name =   'home/resume_foundation.html'  

# para el prototipo--------------------------------------------------------
   
class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'inicio.html'   
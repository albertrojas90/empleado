from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm

#tenemos que importar el modelo empleado para poder interceptar los datos
from applications.empleados.models import Empleado
from .models import Departamento


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'
    


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('Estamos en el form_valid')
        # como departamento es una clave foranea muchos a muchos, se necesita crear una instancia para poder
        # hacer el registro
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()# aqui ya se guarda en la base de datos

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        #para hacer un registro de empleado se usa el orm de django
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView,self).form_valid(form)
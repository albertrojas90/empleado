from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
    
from .models import Empleado
from .forms import EmpleadoForm

#Requerimientos
# 1 Lista todos los empleados de la empresa
# 2 Listar todos los empleados que pertenecen a un area de la empresa
# 3 Listar empleados por trabajo
# 4 listar los empleados por palabra clave
# 5 listar las habilidades de un empleado


# 1 Lista todos los empleados de la empresa
class  ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    #Aquí hacemos paginacion
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        print('***********')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        print('lista resultado: ',lista)
        return lista


class  ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados.html'
    #Aquí hacemos paginacion
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

           



    # model = Empleado
    # context_object_name = 'lista_albert'

    # queryset = Empleado.objects.filter(...)
    # for empleado in queryset:
    #     print(empleado)
    #     print(empleado.firts_name)

   
    

# 2 Listar todos los empleados que pertenecen a un area de la empresa

#forma 1
# class ListByAreaEmpleado(ListView):
#      """ Lista empleados de un area """
#      template_name = 'empleados/list_by_area.html'
#      queryset = Empleado.objects.filter(
#          departamento__name = 'TESTER'
#      )

# forma 2
class ListByAreaEmpleado(ListView):
     """ Lista empleados de un area """
     template_name = 'empleados/list_by_area.html'
     context_object_name = 'empleados'
    
     def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
         departamento__name = area
        )
        return lista   
     
# 4 listar los empleados por palabra clave

class ListEmpleadosByKword(ListView):
    """ lista de empleados por palabra clave """
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleadus'

    def get_queryset(self):
        print('***********')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado: ',lista)
        return lista

# 5 listar las habilidades de un empleado

class ListHabiliadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=12)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()


# 3 Listar empleados por trabajo: por revisarrrrrr

class ListByTrabajo(ListView):
    """ Lista empleados por trabajo """
    template_name ='empleados/list_by_trabajo.html'
    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = trabajo
        )  
        return lista
    
   # ---------------A parti de aquí DetalView---------------------

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/detail_empleado.html'
   
    def get_context_data(self, **kwargs):
         context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
         context['titulo'] = 'empleado del mes'
         return context 


#---------------- a partir de aquí vista CreateView-----------------------

class EmpleadoCreateView(CreateView):
    template_name = 'empleados/add.html'
    model = Empleado
    form_class = EmpleadoForm
    # forma 1 de traer todos los campos del modelo empleado
    #fields = ['first_name','last_name','job', 'departamento','habilidades', 'avatar',]
    #forma2
    #fields = ('__all__')
    # URL donde se va a redireccionar una vez completado el proceso. Se recargue la misma pagina.
    success_url= reverse_lazy('empleado_app:empleado_add')

    def form_valid(self, form) :
        #logica del proceso
        empleado = form.save(commit=False)# se recupera una instancia del formulario pero con una instancia a la base de datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        #luego se hace la actualización a la base de datos de ese full_name
        empleado.save()
        print('variable empleado posee')
        print(empleado)
        return super(EmpleadoCreateView,self).form_valid(form)


#--------- para redireccionar a otra pagina-----------------------
class SuccessView(TemplateView):
    template_name = "empleados/success.html"

#--------------para realizar actualizaciones con UpdateView-----------------Empleado

class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = ['first_name','last_name','job', 'departamento','habilidades']
      # URL donde se va a redireccionar una vez completado el proceso. Se recargue la misma pagina.
    success_url= reverse_lazy('empleado_app:empleados_admin')

    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        print('*****************METODO POST*************')
        print('*****************************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request,*args,**kwargs)


    def form_valid(self, form) :
       print('*********METODO FORM VALID************')
       print('*****************************************')
       return super(EmpleadoUpdateView,self).form_valid(form)


#-------------------------Para eliminar DeleteView--------------------------------
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url= reverse_lazy('empleado_app:empleados_admin')
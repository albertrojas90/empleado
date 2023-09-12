from django.urls import path
from django.contrib import admin
from . import views

# se usa para darle un name a este conjunto de urls
app_name = "empleado_app"


urlpatterns = [
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(), 
        name = 'empleados_all'
        ),
    path('listar-by-area/<name>/', 
         views.ListByAreaEmpleado.as_view(),
           name= 'empleados_area'
           ),
    path('listar-empleados-admin/', 
         views.ListaEmpleadosAdmin.as_view(),
           name= 'empleados_admin'
        ),       
    path('listar-by-trabajo/<job>/', views.ListByTrabajo.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabiliadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(), 
        name = 'empleado_detail'
        ),
    path('add-empleado/',
          views.EmpleadoCreateView.as_view(),
            name = 'empleado_add'
        ),
    path('success/', views.SuccessView.as_view(), name= 'correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),  
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'), 
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name= 'inicio'),
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.MODELPruebaListView.as_view()),
    path('lista-prueba/', views.MODELPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name = 'prueba_add'),
    path('home-prueba/', views.PruebaView.as_view(), name = 'prueba_view'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name = 'resume_foundation'),
]

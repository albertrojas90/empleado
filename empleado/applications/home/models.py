from django.db import models

# Create your models here.

#para crear un modelo de bases de datos, usamos siempre clases y siempre se va a usar herencias
#aqui estariamos creando una tabla con dos atributos
class Prueba(models.Model):
    #aquí irian los atributos de la tabla
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.titulo + '-' + self.subtitulo 

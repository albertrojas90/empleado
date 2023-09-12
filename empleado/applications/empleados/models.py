from django.db import models
#para hacer la conexión con la tabla departamento se debe hacer la importación
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','INGENIERO'),
        ('4','OTRO'),
    )

    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('apellidos',max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null = True)
    #para relación muchos a muchos m2m
    full_name = models.CharField(
        'Nombre completos',
        max_length= 120,
        blank= True
    )
    habilidades = models.ManyToManyField(Habilidades)# una habilidad le pertenece a un empleado, y un empleado puede tener muchas habilidades
    #hoja_vida = RichTextField()
   
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name','last_name']
        unique_together = ('first_name','departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
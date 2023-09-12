# Generated by Django 4.2.4 on 2023-08-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]

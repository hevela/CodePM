from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    STATUS = (
        ('Estimación', 'Estimación'),
        ('Planeación', 'Planeación'),
        ('En progreso', 'En progreso'),
        ('En entrega', 'En entrega'),
        ('Terminado', 'Terminado'),
    )
    name = models.CharField(max_length=128, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Descripción')
    status = models.TextField(choices=STATUS, default=STATUS[0][0])

    def __str__(self):
        return self.name + self.status


class Participant(models.Model):
    team_member = models.ForeignKey(User, verbose_name='Miembro del equipo')
    project = models.ForeignKey(Project, verbose_name='Proyecto')

    def __str__(self):
        return self.team_member.get_full_name() + ' - ' + self.project.name


class StatusFeature(models.Model):
    status = models.CharField(max_length=64, verbose_name='Status')


class Iteration(models.Model):
    iteration = models.CharField(max_length=64, verbose_name='Iteración')
    project = models.ForeignKey(Project, verbose_name='Proyecto')
    start = models.DateTimeField(null=True, blank=True, verbose_name='Inicio')
    end = models.DateTimeField(null=True, blank=True, verbose_name='Fin')

    def __str__(self):
        return self.iteration + ' - ' + (self.project)


class Feature(models.Model):
    FEATURE_STATUS = (
        ('Backlog', 'Backlog'),
        ('En progreso', 'En progreso'),
        ('En revisión', 'En Revisión'),
        ('Terminado', 'Terminado')
    )
    feature = models.CharField(max_length=128, verbose_name='Feature')
    description = models.TextField(
        null=True, blank=True, verbose_name='Descripción')
    iteration = models.ForeignKey(
        Iteration, verbose_name='Iteración', blank=True, null=True)
    end_date = models.DateField(
        null=True, blank=True, verbose_name='Terminado el')
    status = models.CharField(max_length=64, verbose_name='Status')

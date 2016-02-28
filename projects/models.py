from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Descripción')

    def __str__(self):
        return self.name


class Participant(models.Model):
    team_member = models.ForeignKey(User, verbose_name='Miembro del equipo')
    project = models.ForeignKey(Project, verbose_name='Proyecto')

    def __str__(self):
        return self.team_member.get_full_name() + ' - ' + self.project.name

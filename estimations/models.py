from django.db import models

from projects.models import Project, Feature


class Estimation(models.Model):
    project = models.ForeignKey(Project, verbose_name='Proyecto')
    tentative_start = models.DateField(verbose_name='Fecha Tentativa de Inicio')
    dev_number = models.SmallIntegerField(
        default=1, verbose_name='Num. de Developers')
    team_availability = models.SmallIntegerField(
        default=1, verbose_name='Disponibilidad del equipo')

    def __str__(self):
        return self.project.name + ' - ' + str(self.tentative_start)


class FeatureStimation(models.Model):
    estimation = models.ForeignKey(Estimation, verbose_name='Estimación')
    feature = models.ForeignKey(Feature, verbose_name='Feature')
    estimated_hours = models.SmallIntegerField(
        default=1, verbose_name='Tiempo estimado (Hrs)')
    multiplier = models.SmallIntegerField(
        default=1, verbose_name='Multiplicador')
    qa_estimated_hours = models.SmallIntegerField(
        default=1, verbose_name='Tiempo estimado Testing (Hrs)')
    qa_multiplier = models.SmallIntegerField(
        default=1, verbose_name='Multiplicador Testing')

    def __str__(self):
        return self.estimation + ' - ' + self.estimated_hours

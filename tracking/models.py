from django.db import models

from projects.models import Participant


class Tracking(models.Model):
    participant = models.ForeignKey(
        Participant, verbose_name='Participante del Proyecto')
    day = models.DateField(verbose_name='Día')
    hours = models.SmallIntegerField(null=True, blank=True,
                                     verbose_name='Horas invertidas')
    notes =  models.TextField(
        null=True, blank=True, verbose_name='Notas o comentarios')

    def __str__(self):
        s = [
            str(self.participant),
            ' - ',
            str(self.date),
            ' - ',
            str(self.hours)
        ]
        return ''.join(s)

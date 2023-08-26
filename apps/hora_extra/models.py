from django.db import models
from apps.empregados.models import Empregado


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    empregado = models.ForeignKey(Empregado, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.motivo
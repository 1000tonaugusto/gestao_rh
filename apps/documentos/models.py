from django.db import models
from apps.empregados.models import Empregado


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Empregado, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

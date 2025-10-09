from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - Nota: {self.nota}"



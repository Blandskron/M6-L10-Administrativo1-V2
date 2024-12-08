from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    publicado_en = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

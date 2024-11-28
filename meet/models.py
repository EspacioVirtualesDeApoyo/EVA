from django.db import models

class EncuentroSincronico(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    url = models.URLField(max_length=200, blank=True, null=True)  # Campo de URL opcional

    def __str__(self):
        return self.nombre

from django.db import models

# Create your models here.

class mercadeo1(models.Model):
    cantidad_registrada = models.PositiveSmallIntegerField()
    cantidad_vendida = models.PositiveSmallIntegerField()
    ganancia = models.PositiveSmallIntegerField()
    empresa_transporte = models.CharField(max_length=30)
    stock_minimo = models.PositiveSmallIntegerField()
    fecha_compra = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.cantidad_registrada}'
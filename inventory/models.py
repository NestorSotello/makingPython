# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# se crea los modelos y las clases heredan los mismos campos


class Dispositivo(models.Model):
    # nombre de la columna de la base de datos
    tipo = models.CharField(max_length=100, blank=False)
    precio = models.IntegerField()

    choices = (
        ('disponible', 'Item listo'),
        ('Vendido', 'Item Vendido'),
        ('Reponer', 'Reponer Item en la brevedad')
    )

    # disponible, vendido, reponer stock, etc

    estado = models.CharField(
        max_length=10, choices=choices, default='Vendido')
    comentario = models.CharField(max_length=100, default="Sin Comentarios")

    class Meta:
        abstract = True

    def __str__(self):
        return 'tipo:{0} precio:{1}'.format(self.tipo, self.precio)


# aca podemos agregar
class laptop(Dispositivo):
    pass


class Desktop(Dispositivo):
    pass


class Telefono(Dispositivo):
    pass


# luego de crear los modelos se ejecuta el comando python manage.py makemigrations y crea las tablas
# y luego ejecutar el comando python manage.py migrate y crea la base de datos

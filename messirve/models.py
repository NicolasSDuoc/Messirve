# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=450, blank=True, null=True)
    imagen = models.ImageField(upload_to='adjunt',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CommaSeparatedIntegerField
from django.utils.timezone import now

# Create your models here.

#Datos de la tabla index
class Pais(models.Model):

    nombre = models.CharField(max_length=255)
    

    def __str__(self):
        return str(self.nombre) 

class Exportador (models.Model):
    pais = models.ForeignKey(to=Pais, on_delete=models.CASCADE, )
    nombre = models.CharField(max_length=255)
    rut=models.CharField(max_length=255)

    def __str__(self):
        return str(self.nombre) + ' || ' + str(self.rut) + ' || '+ str(self.pais)


class Importador (models.Model):
    pais = models.ForeignKey(to=Pais, on_delete=models.CASCADE, )
    nombre = models.CharField(max_length=255)
    rut=models.CharField(max_length=255)
    def __str__(self):
        return str(self.nombre) +' || '+ str(self.rut)+ ' || ' + str(self.pais)

class Producto ( models.Model):
    descripcion= models.CharField(max_length=255)
    precio= models.IntegerField()

    def __str__(self):
        return str(self.descripcion) + ' || ' + str(self.precio)

class Detalle (models.Model):
    importador = models.ForeignKey(to=Importador, on_delete=models.CASCADE)
    exportador = models.ForeignKey(to=Exportador, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto , on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    tipo_transporte = models.CharField(max_length=255)
    fecha = models.DateField(default=now)

    def __str__(self):
        return str(self.importador) + ' || ' + str(self.exportador) + ' || ' + str(self.producto)

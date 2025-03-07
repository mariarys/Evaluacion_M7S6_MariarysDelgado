from django.db import models

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    pais = models.CharField(max_length = 100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    f_vencimiento = models.DateField(null = True, blank = True)
    fabricante = models.ForeignKey (Fabricante, on_delete=models.CASCADE, related_name='productos',null=True )

    def __str__(self):
        return f"{self.nombre} - {self.fabricante.nombre}"
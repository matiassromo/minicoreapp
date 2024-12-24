from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, default='Sin descripcion')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
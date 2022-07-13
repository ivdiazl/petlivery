from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos",null=True)
    
    def __str__(self):
        return self.nombre
    
opciones_consultas = [
    [0, "consulta"],
    [0, "reclamo"],
    [0, "sugerencia"],
    [0, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre


class Tipo_animal(models.Model):
    nombreA = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreA
    
class Animal(models.Model):
    nombreA = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    tipo_animal = models.ForeignKey(Tipo_animal, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombreA
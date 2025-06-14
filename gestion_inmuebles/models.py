
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

TIEMPO_CHOICES = [
    ('Por_hora', 'Por hora'),
    ('Por_semana', 'Por semana'),
    ('Por_mes', 'Por mes'),
    ('Por_noche', 'Por noche'),
]

ESTADO_CHOICES = [
    ('Disponible', 'Disponible'),
    ('No_disponible', 'No disponible'),
    ('Mantenimiento', 'En mantenimiento'),
]

TIPO_COCHERA_CHOICES = [
    ('Cubierta', 'Cubierta'),
    ('Descubierta', 'Descubierta'),
]

class Inmueble(models.Model):
    activo = models.BooleanField(default=True)
    tipo = models.CharField(default='-', max_length=20, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    calle = models.CharField(max_length=100, default="-")
    numero = models.PositiveIntegerField(default=0)
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    politica_cancelacion = models.TextField(blank=True)
    estado = models.CharField(default='Disponible', choices=ESTADO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo = models.CharField(default='-', choices=TIEMPO_CHOICES)
    imagen = models.ImageField(upload_to='inmuebles/', blank=True, null=True)
    superficie = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    


class InmueblesSimilares(Inmueble):
    tiene_internet = models.BooleanField(default=False)
    banios = models.PositiveIntegerField(default=0)
    tiene_cochera = models.BooleanField(default=False)
    habitaciones = models.PositiveIntegerField(default=0)


class Departamento(InmueblesSimilares):
    piso = models.PositiveIntegerField(null=True, blank=True)
    cantidad_inquilinos = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        self.tipo = "Departamento"
        super().save(*args, **kwargs)


class Casa(InmueblesSimilares):
    pisos = models.PositiveIntegerField(null=True, blank=True)
    cantidad_inquilinos = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        self.tipo = "Casa"
        super().save(*args, **kwargs)


class Local(InmueblesSimilares):
    frente = models.DecimalField(max_digits=10, decimal_places=2)
    fondo = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.tipo = "Local"
        super().save(*args, **kwargs)


class Cochera(Inmueble):
    tipo_cochera = models.CharField(default='-', choices=TIPO_COCHERA_CHOICES)
    largo_plaza = models.DecimalField(max_digits=10, decimal_places=2)
    ancho_plaza = models.DecimalField(max_digits=10, decimal_places=2)
    plazas = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.tipo = "Cochera"
        super().save(*args, **kwargs)
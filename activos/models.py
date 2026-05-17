from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Activo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)  
    nombre = models.CharField(max_length=100)              
    descripcion = models.TextField()                        
    ESTADOS = [                                             
        ("Disponible", "Disponible"),
        ("Asignado", "Asignado"),
        ("Mantenimiento", "Mantenimiento"),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Disponible"                             
    )

    def __str__(self):
        # Lo que se mostrará en el admin y listas
        return f"{self.codigo} - {self.nombre} ({self.estado})"



class Asignacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)  
    fecha_entrega = models.DateField(default=timezone.now)        

    def __str__(self):

        return f"{self.activo.codigo} - {self.usuario.first_name} ({self.activo.estado})"

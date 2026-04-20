from django.db import models

class Curso(models.Model):
    STATUS_CHOICES = [('Activo', 'Activo'), ('Inactivo', 'Inactivo')]

    nombre = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    clave = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(verbose_name="Descripción")
    costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo ($)")
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración (Horas)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Activo')
    imagen_url = models.URLField(blank=True, help_text="URL de una imagen para el curso")

    def __str__(self):
        return f"{self.clave} - {self.nombre}"

class PreInscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    nombre = models.CharField(max_length=200, verbose_name="Nombre Completo")
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} -> {self.curso.nombre}"

# FUNCIONALIDAD ADICIONAL (Bonus): Sistema de Reseñas
class Resena(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='resenas')
    autor = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Estrellas")
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.autor} para {self.curso.nombre}"
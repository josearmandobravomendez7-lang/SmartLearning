from django.contrib import admin
from .models import Curso, PreInscripcion, Resena

# Configuramos el panel de administrador para las Altas, Bajas, Consultas y Modificaciones
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'costo', 'fecha_inicio', 'status')
    list_filter = ('status', 'fecha_inicio')
    search_fields = ('nombre', 'clave')

@admin.register(PreInscripcion)
class PreInscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso', 'correo', 'ciudad', 'fecha_registro')
    list_filter = ('curso', 'estado')
    search_fields = ('nombre', 'correo')

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'autor', 'calificacion', 'fecha_creacion')
    list_filter = ('calificacion',)
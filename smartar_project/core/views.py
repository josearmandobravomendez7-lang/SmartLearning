from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Curso, PreInscripcion, Resena

def home(request):
    # Página informativa de la empresa
    return render(request, 'core/home.html')

def catalogo(request):
    # Catálogo de cursos disponibles
    cursos = Curso.objects.filter(status='Activo').order_by('fecha_inicio')
    return render(request, 'core/catalogo.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    # Detalles, conteo de alumnos y funcionalidad extra (Reseñas)
    curso = get_object_or_404(Curso, id=curso_id)
    inscritos_count = curso.inscripciones.count()
    resenas = curso.resenas.all().order_by('-fecha_creacion')

    if request.method == 'POST':
        # Procesamiento del formulario de Pre-inscripción
        if 'btn_inscripcion' in request.POST:
            PreInscripcion.objects.create(
                curso=curso,
                nombre=request.POST['nombre'],
                correo=request.POST['correo'],
                telefono=request.POST['telefono'],
                ciudad=request.POST['ciudad'],
                estado=request.POST['estado']
            )
            messages.success(request, '¡Pre-inscripción realizada con éxito! Nos pondremos en contacto pronto.')
            return redirect('detalle_curso', curso_id=curso.id)

        # Procesamiento de la Funcionalidad Adicional (Nueva Reseña)
        elif 'btn_resena' in request.POST:
            Resena.objects.create(
                curso=curso,
                autor=request.POST['autor'],
                calificacion=request.POST['calificacion'],
                comentario=request.POST['comentario']
            )
            messages.success(request, '¡Gracias por compartir tu reseña!')
            return redirect('detalle_curso', curso_id=curso.id)

    return render(request, 'core/detalle_curso.html', {
        'curso': curso,
        'inscritos_count': inscritos_count,
        'resenas': resenas
    })
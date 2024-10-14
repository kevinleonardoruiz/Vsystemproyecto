from django.shortcuts import render, redirect
from .models import EstudianteCurso
from .forms import EstudianteCursoForm
from django.shortcuts import render, get_object_or_404, redirect

from curso.models import curso  

# Vista para listar los estudiantes y cursos
def Estudiante_Curso(request):
    cursos = curso.objects.all()  # Obtener todos los cursos disponibles
    curso_seleccionado = request.GET.get('curso')  # Obtener el curso seleccionado del filtro (si hay)

    if curso_seleccionado:
        estudiantes_cursos = EstudianteCurso.objects.filter(curso=curso_seleccionado)  # Filtrar por curso seleccionado
    else:
        estudiantes_cursos = EstudianteCurso.objects.all()  # Mostrar todos si no se selecciona un curso

    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudiantes_cursos,
        'cursos': cursos,  # Pasar los cursos a la plantilla
        'curso_seleccionado': curso_seleccionado  # Pasar el curso seleccionado a la plantilla
    })
# Vista para agregar o editar una relación de estudiante con curso
def formulario_estudiante_curso(request):
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario
            return redirect('lista-estudiantes-cursos')  # Asegúrate de que este nombre coincida
    else:
        form = EstudianteCursoForm()  # Formulario vacío si no es POST

    return render(request, 'formulario_estudiante_curso.html', {'form': form})

def eliminar_estudiante_curso(request, id):
    relacion = get_object_or_404(EstudianteCurso, id=id)
    relacion.delete()
    return redirect('lista-estudiantes-cursos')  


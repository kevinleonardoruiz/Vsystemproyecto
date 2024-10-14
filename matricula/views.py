from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm  
from django.shortcuts import render, get_object_or_404, redirect

from curso.models import curso  # Importar el modelo Curso para mostrar la lista de cursos

def lista_matriculas(request):
    cursos = curso.objects.all()  # Obtener todos los cursos disponibles
    curso_seleccionado = request.GET.get('curso')  # Obtener el curso seleccionado del filtro

    if curso_seleccionado:
        matriculas = Matricula.objects.filter(estudiante_curso__curso=curso_seleccionado)  # Filtrar por curso seleccionado
    else:
        matriculas = Matricula.objects.all()  # Mostrar todas las matrículas si no se selecciona un curso

    return render(request, 'lista_matricula.html', {
        'title': 'Lista de matrículas',
        'matriculas': matriculas,
        'cursos': cursos,  # Pasar los cursos a la plantilla
        'curso_seleccionado': curso_seleccionado  # Pasar el curso seleccionado a la plantilla
    })

def formulario_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-matriculas')  
    else:
        form = MatriculaForm()  

    return render(request, 'formulario_matricula.html', {'form': form})

def eliminar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('lista-matriculas')
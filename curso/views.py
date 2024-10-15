from django.shortcuts import render, redirect
from .models import curso
from .forms import CursoForm
from django.shortcuts import render, get_object_or_404, redirect


def get_curso(request):
    cursos = curso.objects.all()
    return render(request, 'lista_cursos.html', {
        'title': 'Lista de cursos',
        'cursos': cursos,
    })

def formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-cursos')  
    else:
        form = CursoForm()

    return render(request, 'formulario_curso.html', {'form': form})

def eliminar_curso(request, id):
    estudiante = get_object_or_404(curso, id=id)
    estudiante.delete()
    return redirect('lista-cursos')
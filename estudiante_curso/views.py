from django.shortcuts import render, redirect
from .models import EstudianteCurso
from .forms import EstudianteCursoForm
from django.shortcuts import render, get_object_or_404, redirect

from curso.models import curso  


def Estudiante_Curso(request):
    cursos = curso.objects.all()  
    curso_seleccionado = request.GET.get('curso')  

    if curso_seleccionado:
        estudiantes_cursos = EstudianteCurso.objects.filter(curso=curso_seleccionado)  
    else:
        estudiantes_cursos = EstudianteCurso.objects.all()  

    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudiantes_cursos,
        'cursos': cursos,  
        'curso_seleccionado': curso_seleccionado  
    })


def formulario_estudiante_curso(request):
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-estudiantes-cursos')  
    else:
        form = EstudianteCursoForm()  

    return render(request, 'formulario_estudiante_curso.html', {'form': form})

def eliminar_estudiante_curso(request, id):
    relacion = get_object_or_404(EstudianteCurso, id=id)
    relacion.delete()
    return redirect('lista-estudiantes-cursos')  


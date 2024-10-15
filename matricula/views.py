from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm  
from django.shortcuts import render, get_object_or_404, redirect

from curso.models import curso  

def lista_matriculas(request):
    cursos = curso.objects.all() 
    curso_seleccionado = request.GET.get('curso')  

    if curso_seleccionado:
        matriculas = Matricula.objects.filter(estudiante_curso__curso=curso_seleccionado)  
    else:
        matriculas = Matricula.objects.all()  

    return render(request, 'lista_matricula.html', {
        'title': 'Lista de matrículas',
        'matriculas': matriculas,
        'cursos': cursos,  
        'curso_seleccionado': curso_seleccionado
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
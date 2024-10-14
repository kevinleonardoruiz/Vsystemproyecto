from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

# Vista para listar estudiantes
def get_estudiantes(request):
    estudiantes = Persona.objects.filter(rol='Estudiante')
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False) 
            estudiante.rol = 'Estudiante'  
            estudiante.save()  
            return redirect('lista-estudiantes')  
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiante.html', {'form': form})

def eliminar_estudiante(request, dni):
    estudiante = get_object_or_404(Persona, dni=dni)
    estudiante.delete()
    return redirect('lista-estudiantes')

def eliminar_profesor(request, profesor_id):
    profesor_instance = get_object_or_404(Persona, id=profesor_id)
    profesor_instance.delete()
    return redirect('lista-profesores')

def formulario_profesor(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.rol = 'Profesor'  # Asignar el rol predeterminado
            profesor.save()  # Guardar el nuevo profesor
            return redirect('lista-profesores')  # Redirigir a la lista de profesores
    else:
        form = PersonaForm()

    return render(request, 'formulario_profesor.html', {'form': form})
def get_profesores(request):
    profesores = Persona.objects.filter(rol='Profesor')
    return render(request, 'lista-profesores.html', {
        'title': 'Lista de profesores',
        'profesores': profesores
    })

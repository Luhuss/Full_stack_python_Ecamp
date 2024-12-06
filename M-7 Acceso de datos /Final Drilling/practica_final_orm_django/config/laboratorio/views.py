from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Laboratorio, DirectorGeneral, Producto

from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm

# Create your views here.

# views o controller para listar laboratorios
def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar_laboratorios.html', {'laboratorios': laboratorios})

# views o controller para crear laboratorios
def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio creado')
            return redirect('listar_laboratorio')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_laboratorio'))
    else:
        form = LaboratorioForm()
        return render(request, 'crear_laboratorio.html', {'form':form}) 

# views o controller para editar laboratorios

# views o controller para eliminar laboratorios

# views o controller para registro

# views o controller para login

# views o controller para logout


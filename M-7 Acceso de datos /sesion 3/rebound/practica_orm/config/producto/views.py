from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm
import datetime

# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'

def listar(request):
    #productos = Producto.objects.all().values().filter(precio__lte=2500).values('nombre', 'precio')
    productos = Producto.objects.using('default').all().order_by('id')
    return render(request, 'listar_producto.html', {'productos': productos})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar los datos ingresados.')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form': form})

def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form = form.save(commit=False)
            form.fecha_modificacion = datetime.datetime.now()
            form.save()
            messages.success(request, 'Producto editado exitosamente.')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar los datos para la edición.')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto_id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'producto_form': form, 'producto_id': producto_id})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  
    producto.delete()
    messages.info(request, 'Producto eliminado exitosamente.')
    return redirect('listar_producto')

def index(request):
    return render(request, 'index.html')

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        try:
            query_id = int(query)
        except ValueError:
            query_id = None
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) | 
            (Q(id=query_id) if query_id is not None else Q())
            ).order_by('id')
        return render(request, 'listar_producto.html', {'productos':productos})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar_producto')
        else:
            messages.error(request, 'Usuario o password inválidos')
            form = AuthenticationForm()
            return render(request, 'login.html', {'form':form}) 
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})  
    
def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def registro(request):   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro éxitoso')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Datos inválidos')
            form = UserCreationForm()
            return render(request, 'registro.html', {'form':form}) 
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form':form})
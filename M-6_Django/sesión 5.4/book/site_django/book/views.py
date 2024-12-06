from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import Book
from .forms import BookForm
import datetime 


# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'
    
@login_required # para que solo se pueda acceder si estan logeados
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

# https://docs.djangoproject.com/en/5.1/topics/forms/
@login_required
def crear_libro(request):
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST)
        if form.is_valid(): # si el formulario es valido
            form.save() # guarda los datos en la base de datos
            messages.success(request, 'libro creado correctamente') # muestra un mensaje de 'libro creado correctamente'
            return redirect('lista_libros') # redirecciona a lista_libros
        else: # si el formulario no es valido
            messages.error(request, 'Modifica los datos de ingreso') # muestra un mensaje
            return HttpResponseRedirect(reverse('crear_libro')) # redirecciona a la pagina
    else: # si el metodo es GET
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})

@login_required
def editar_libro(request, libro_id):
    # https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
    # https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la db o status 404 not found
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) # instancia del formulario con los datos del libro a editar
        if form.is_valid(): # si el formulario es valido
            book = form.save(commit=False) # pre guardado de los datos
            book.fecha_modificacion = datetime.datetime.now() # guarda la fecha de modificacion
            book.save() # guarda los datos en la base de datos
            messages.success(request, 'libro editado correctamente') # muestra un mensaje de 'libro editado correctamente'
            return redirect('lista_libros') # redirecciona a lista de libros
        else: # si el formulario no es valido
            messages.error(request, 'Modifica los datos de ingreso') # muestra un mensaje
            return HttpResponseRedirect(reverse('editar_libro', args=[book.id])) # redirecciona a la pagina
    else: # si el metod es GET
        form = BookForm(instance=book) # instancia del formulario con los datos del libro a editar
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id}) # renderiza la vista para editar el libro 

@login_required
def eliminar_libro(request, libro_id):
    book = get_object_or_404(Book, pk=libro_id) # obteniendo el libro a eliminar en la db o status 404 not found
    book.delete() # eliminando el libro de la base de datos
    messages.info(request, 'Libro eliminado correctamente') # muestra mensaje
    return redirect('lista_libros') # redirecciona a la lista de libros

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # guardando los datos del usuario en una variable
            
            content_type = ContentType.objects.get_for_model(Book)
            permission = Permission.objects.get(
            codename='development',
            content_type=content_type,
            )
            
            user.user_permissions.add(permission)
            #user.save() # guardando los datos del usuario en la base de datos
            
            messages.success(request, 'Registro exitoso')
            return redirect('login') # cambiar a login
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})
    
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # autentica el usuario en la db
        if user is not None: 
            login(request, user) # persistir la sesion del usuario 
            return redirect('lista_libros') # redireccionar a ruta seleccionada
        else:
            messages.error(request, 'Credenciales inválidas')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')
    
    
def home_page(request):
    return render(request, 'index.html')

@login_required
def cerrar_sesion(request):
    logout(request) # cierra la sesion
    return render(request, 'index.html')

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        book = Book.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query)).order_by('id')
        return render(request, 'lista_libros.html', {'book':book})
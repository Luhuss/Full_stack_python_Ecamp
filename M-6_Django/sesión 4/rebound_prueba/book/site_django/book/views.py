from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("¡Hola, bienvenido a mi primer proyecto en Django!")

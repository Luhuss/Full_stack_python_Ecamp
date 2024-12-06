from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("¡Hola, bienvenido a mi primer proyecto en Django!")

class IndexPageView(TemplateView): 
    template_name = 'index.html'
    
def palindromo(request, palabra):
    palabra_sin_espacios = palabra.replace(' ', ' ')
    if palabra_sin_espacios == palabra_sin_espacios[::-1] :
        es_palindromo = 'es palindromo'
    else: 
        es_palindromo = 'NO ES PALINDROMO'
        
    context = {'es_palindromo': es_palindromo}
        
    return render(request, 'espalindromo.html', context)

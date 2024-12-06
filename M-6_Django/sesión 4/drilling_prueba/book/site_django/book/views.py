from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido al sitio de libros")

class IndexPageView(TemplateView):
    template_name = 'index.html'

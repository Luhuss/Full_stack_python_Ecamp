from django.urls import path
from .views import listar, crear, editar

urlpatterns = [
    #path('', IndexPageView.as_view(), name="index"),
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
    path('editar_producto/<int:producto_id>', editar, name='editar'),
]
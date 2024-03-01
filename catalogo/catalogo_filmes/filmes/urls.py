from django.urls import path
from .views import cadastrar_filme, listar_filmes, excluir_filme, editar_filme

urlpatterns = [
    path('', cadastrar_filme, name='cadastrar_filme'),
    path('listar/', listar_filmes, name='listar_filmes'),
    path('editar/<int:filme_id>/', editar_filme, name='editar_filme'),
    path('excluir/<int:filme_id>/', excluir_filme, name='excluir_filme'),

]

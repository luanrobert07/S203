from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
from .forms import FilmeFilterForm

def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/cadastrar_filme.html', {'form': form})

def listar_filmes(request):
    filmes = Filme.objects.all()

    # Processar o formulário de filtro e ordenação
    form = FilmeFilterForm(request.GET)
    if form.is_valid():
        ordenar_por = form.cleaned_data['ordenar_por']
        filmes = filmes.order_by(ordenar_por)

        filtro_genero = form.cleaned_data['filtro_genero']
        if filtro_genero:
            filmes = filmes.filter(genero__icontains=filtro_genero)

        filtro_diretor = form.cleaned_data['filtro_diretor']
        if filtro_diretor:
            filmes = filmes.filter(diretor__icontains=filtro_diretor)

    context = {'filmes': filmes, 'form': form}
    return render(request, 'filmes/listar_filmes.html', context)

def editar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    # Lógica para edição do filme
    return render(request, 'filmes/editar_filme.html', {'filme': filme})

def excluir_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    # Lógica para exclusão do filme
    filme.delete()
    return redirect('listar_filmes')  # Redirecione para a página de listagem após excluir

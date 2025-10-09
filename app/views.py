from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Filme

def lista_filmes(request):
    if request.method == "POST":
        
        if 'remover_filme_id' in request.POST:
           
            filme_id = request.POST.get("remover_filme_id")
            filme = get_object_or_404(Filme, id=filme_id)
            filme.delete()
            messages.success(request, f'Filme "{filme.titulo}" removido com sucesso!')
        else:
            
            titulo = request.POST.get("titulo")
            descricao = request.POST.get("descricao")
            nota = request.POST.get("nota")

            if titulo:
                Filme.objects.create(titulo=titulo, descricao=descricao, nota=nota)
                messages.success(request, f'Filme "{titulo}" adicionado com sucesso!')

    filmes = Filme.objects.all()
    return render(request, 'filmes.html', {'filmes': filmes})



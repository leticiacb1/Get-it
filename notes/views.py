from asyncio.windows_events import NULL
from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    # return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
    # Carregando entradas da tabela
    # objcts é um objeto do tipo Django que permite a interação com o bd.
    # all() lista todas as entradas, temos filter() , o get () etc.

    all_notes = Note.objects.all() 
    all_tags = Tag.objects.all()

    if (request.method == 'GET'):
        return render(request, 'notes/index.html', context = {'anotacoes': all_notes , 'tags': all_tags})

    elif (request.method == 'POST'):

        title = request.POST.get('titulo')
        content = request.POST.get('detalhes') 
        # Tag é opcional:
        tag = request.POST.get('tag')

        # Verifica se o valor da Tag não é vazio:
        if tag != NULL or tag != "":
            tag  = Tag(tag_name = tag)
            tag.save()

        nova_nota = Note(title = title, content = content, tag= tag)
        nova_nota.save()

        return redirect('index')

# Novas rotas, argumento actions do formulário.
def deletar(request):
    
    #  Pegando id, enviado pelo input id do formulário.
    id = request.POST.get('id')

    note_to_delete = Note.objects.get(id=id)
    note_to_delete.delete()

    return redirect('index')

def deletar_tudo(request):

    Note.objects.all().delete()
    Tag.objects.all().delete()
    
    return redirect('index')

def atualizar(request):

    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    id = request.POST.get('id_notEdit')
    # Tag, ainda não implementado:
    tag = request.POST.get('tag')

    Note.objects.filter(id = id).update(title = title, content=content)

    return redirect('index')
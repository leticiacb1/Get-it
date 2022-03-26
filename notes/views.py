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
        tag = None
        tag_name = request.POST.get('tag')

        # Pegando o nome de todas as Tags existentes:
        tags_existentes = [tag.tag_name for tag in all_tags]
    
        # Verifica se o valor da Tag não é vazio, caso seja, nao adiciona a lista de Tags:
        if tag_name.replace(" ", "") != "":
            # Se a Tag já existe não acrescentar no banco
            if tag_name not in tags_existentes:
                tag  = Tag(tag_name = tag_name)
                tag.save()
            else:
                for tag_existente in all_tags:
                    if(tag_name == tag_existente.tag_name):
                        # Referenciando a tag com mesmo nome já existente no banco de dados:
                        tag = tag_existente

        nova_nota = Note(title = title, content = content, tag = tag)
        nova_nota.save()

        return redirect('index')

def see_all_tags(request):
    
    all_notes = Note.objects.all() 
    all_tags = Tag.objects.all()

    return render(request, 'notes/tag.html', context = {'anotacoes': all_notes , 'tags': all_tags})

# Novas rotas, argumento actions do formulário.
def deletar(request):

    all_notes = Note.objects.all()

    #  Pegando id, enviado pelo input id do formulário.
    id = request.POST.get('id')
    note_to_delete = Note.objects.get(id=id)
    tag_deletada = note_to_delete.tag.tag_name
    note_to_delete.delete()

    # Caso não exista mais notes associadas a uma tag, apagar a tag tambem:
    tags_em_notas = [note.tag.tag_name for note in all_notes]
    if tag_deletada not in tags_em_notas:
        tag_to_delete = Tag.objects.get(tag_name=tag_deletada)
        tag_to_delete.delete()
        
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
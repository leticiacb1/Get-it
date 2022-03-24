from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    # return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
    all_notes = Note.objects.all()  # Carregando entradas da tabela
    # objcts é um objeto do tipo Django que permite a interação com o bd.
    # all() lista todas as entradas, temos filter() , o get () etc.
    notes = {}
    notes['anotacoes'] = all_notes

    if (request.method == 'GET'):
        return render(request, 'notes/index.html', context = notes)

    elif (request.method == 'POST'):
        # Apenas entra nessa condição quando a ideia for criar uma nova nota
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        
        nova_nota = Note(title = title, content = content)
        nova_nota.save()

        #  Tratando de outra forma, por meio do nome do botão e do id enviado pelo value dele.
        # elif('delete' in request.POST):
        #     id = request.POST.get('delete')
            
        #     note_to_delete = Note.objects.get(id=id)
        #     note_to_delete.delete()
        
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
    return redirect('index')

def atualizar(request):

    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    id = request.POST.get('id_notEdit')
    # Tag, ainda não implementado:
    tag = request.POST.get('tag')

    Note.objects.filter(id = id).update(title = title, content=content)

    return redirect('index')
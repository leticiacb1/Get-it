from django.shortcuts import render, redirect
from .models import Note


def index(request):
    # return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
    all_notes = Note.objects.all()  # Carregando entradas da tabela
    # objcts é um objeto do tipo Djanog que permite a interação com o bd.
    # all() lista todas as entradas, temos filter() , o get () etc.
    
    notes = {}
    notes['anotacoes'] = all_notes

    if (request.method == 'GET'):
        return render(request, 'notes/index.html', context = notes)
    elif (request.method == 'POST'):
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        # Add nova nota no banco de dados:
        nova_nota = Note(title = title, content = content)
        nova_nota.save()
        return redirect('index')

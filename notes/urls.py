from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deletar', views.deletar, name='deletar'),             #  Rota acionada pelo forms (action = "deletar")
    path('atualizar', views.atualizar, name='atualizar'),        #  Rota acionada pelo forms (action = "atualizar")
    path('deletar_tudo', views.deletar_tudo, name='deletar_tudo')
]
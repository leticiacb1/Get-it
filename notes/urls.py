from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deletar', views.deletar, name='deletar'),             #  Rota acionada pelo forms (action = "deletar")
    path('atualizar', views.atualizar, name='atualizar'),        #  Rota acionada pelo forms (action = "atualizar")
    path('deletar_tudo', views.deletar_tudo, name='deletar_tudo'),
    path('all_tags', views.see_all_tags, name="ver_todas_tags"),
    path('tag_filtrada', views.tag_filtrada, name="tag_filtrada")
]
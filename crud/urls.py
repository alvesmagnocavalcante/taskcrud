from django.urls import path
from .views import ListaTarefasView, NovaTarefaView, EditaTarefaView, RemoveTarefaView

urlpatterns = [
    path('lista/', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('nova/', NovaTarefaView.as_view(), name='nova_tarefa'),
    path('edita/<int:pk>/', EditaTarefaView.as_view(), name='edita_tarefa'),
    path('remove/<int:pk>/', RemoveTarefaView.as_view(), name='remove_tarefa'),
]

# Importando módulos necessários do Django
from .models import Tarefa
from .forms import TarefaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Classe base para a view de listagem de tarefas
class ListaTarefasView(ListView):
    # Especifica o modelo a ser utilizado
    model = Tarefa
    # Especifica o nome do template a ser utilizado para renderizar a view
    template_name = 'lista_tarefas.html'
    # Especifica o nome da variável de contexto que conterá a lista de tarefas no template
    context_object_name = 'tarefas'

# Classe base para a view de criação de nova tarefa
class NovaTarefaView(CreateView):
    # Especifica o modelo a ser utilizado
    model = Tarefa
    # Especifica o formulário a ser utilizado para a criação da tarefa
    form_class = TarefaForm
    # Especifica o nome do template a ser utilizado para renderizar a view
    template_name = 'nova_tarefa.html'
    # Especifica a URL de redirecionamento após a criação bem-sucedida
    success_url = reverse_lazy('lista_tarefas')

# Classe base para a view de edição de tarefa existente
class EditaTarefaView(UpdateView):
    # Especifica o modelo a ser utilizado
    model = Tarefa
    # Especifica o formulário a ser utilizado para a edição da tarefa
    form_class = TarefaForm
    # Especifica o nome do template a ser utilizado para renderizar a view
    template_name = 'edita_tarefa.html'
    # Especifica a URL de redirecionamento após a edição bem-sucedida
    success_url = reverse_lazy('lista_tarefas')

# Classe base para a view de remoção de tarefa existente
class RemoveTarefaView(DeleteView):
    # Especifica o modelo a ser utilizado
    model = Tarefa
    # Especifica o nome do template a ser utilizado para renderizar a view
    template_name = 'removido.html'
    # Especifica a URL de redirecionamento após a remoção bem-sucedida
    success_url = reverse_lazy('lista_tarefas')
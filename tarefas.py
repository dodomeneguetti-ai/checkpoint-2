lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
        'descricao':descricao,
        'concluida':False
    }
    lista_tarefas.append(tarefa)
def listar_tarefas():
    for tarefas in lista_tarefas:
        print(tarefa ['descricao'])
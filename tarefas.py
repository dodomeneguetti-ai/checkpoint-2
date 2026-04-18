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

def lista_tarefas():
    for i , tarefa in enumerate (lista_tarefas):
        status = "[X]" if tarefa["conclida"]else "[]"
        print (f'(i - status)(tarefa["descricao"])')
def concluir_tarefa(indice):
    try:
    except IndexError:
        print("Indice invalido!")
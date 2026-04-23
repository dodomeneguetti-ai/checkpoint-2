import json

lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {'descricao': descricao, 'concluida': False}
    lista_tarefas.append(tarefa)
    salvar_dados()
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not lista_tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(lista_tarefas, start=1):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{i} - {status} {tarefa['descricao']}")

def concluir_tarefa(indice):
    try:
        lista_tarefas[indice - 1]["concluida"] = True
        salvar_dados()
        print("Tarefa concluída com sucesso!")
    except IndexError:
        print("Erro: Esse número de tarefa não existe!")

def remover_tarefa(indice):
    try:
        tarefa_removida = lista_tarefas.pop(indice - 1)
        salvar_dados()
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    except IndexError:
        print("Erro: Esse número de tarefa não existe!")

def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)

def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
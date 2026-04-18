from tarefas import adicionar_tarefa,lista_tarefas,concluir_tarefa


while true:
    print("_________________________")
    print('__ 1 - Adicionar_________')
    print('__ 2 - Listar____________')
    print('__ 3 - Concluir Tarefa___')
    print('__ 0 - Sair______________')
    print("_________________________")

    opcao = input("escolha")

    if opcao == '1':
        desc = input("Digite uma tarefa: ")
        adicionar_tarefa(desc)
    
    elif opcao == '2':
        listar_tarefas()


    elif opcao == '0':
        break

    elif opcao == "3":
        listar_tarefas()
        i = int(input("Digite o numero da tarefa:"))
        concluir_tarefa(i)

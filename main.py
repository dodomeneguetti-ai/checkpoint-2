from tarefas import adicionar_tarefa,lista_tarefas


while true:
    print('1 - adicionar')
    print('2 - listar')
    print('0 - sair')

    opcao = input("escolha")

    if opcao == '1':
        desc = input("digite uma taarefa: ")
        adicionar_tarefa(desc)
    
    elif opcao == '2':
        listar_tarefas()


    elif opcao == '0':
        break
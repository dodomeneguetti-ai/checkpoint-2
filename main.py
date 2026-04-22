from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, lista_tarefas

while True:
    print("\n" + "="*25)
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Concluir Tarefa")
    print("0 - Sair")
    print("="*25)

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        desc = input("Descrição da tarefa: ")
        adicionar_tarefa(desc)
   
    elif opcao == '2':
        print("\n--- SUAS TAREFAS ---")
        listar_tarefas()

    elif opcao == '3':
        listar_tarefas()
        try:
            i = int(input("Número da tarefa a concluir: "))
            concluir_tarefa(i)
           
        except ValueError:
            print("Por favor, digite um número.")

    elif opcao == '0':
        print("Saindo...")
        break
   
    else:
        print("Opção inválida!")

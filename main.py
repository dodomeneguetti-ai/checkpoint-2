import tarefas as t
import time 


t.carregar_dados()

while True:
    print("\n" + "="*25)
    print("      GERENCIADOR ")
    print("            DE")
    print("         TAREFAS")
    print("="*25)
    print("   1 - Adicionar Tarefa")
    print("   2 - Listar Tarefas")
    print("   3 - Concluir Tarefa")
    print("   4 - Remover Tarefa")
    print("   0 - Sair")
    print("="*25)

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        desc = input("Descrição da tarefa: ")
        t.adicionar_tarefa(desc)
        time.sleep(1.5)
   
    elif opcao == '2':
        print("\n---- SUAS TAREFAS ---")
        t.listar_tarefas()
        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == '3':
        print("\n--- QUAL DESEJA CONCLUIR? ---")
        t.listar_tarefas()
        try:
            i = int(input("\nNúmero da tarefa a concluir: "))
            t.concluir_tarefa(i)
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
        time.sleep(1.5)

    elif opcao == '4':
        print("\n--- QUAL DESEJA REMOVER? ---")
        t.listar_tarefas()
        try:
            i = int(input("\nNúmero da tarefa a remover: "))
            t.remover_tarefa(i)
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
        time.sleep(1.5)

    elif opcao == '0':
        print("Dados salvos. Saindo...")
        time.sleep(1)
        break
   
    else:
        print("Opção inválida!")
        time.sleep(1)
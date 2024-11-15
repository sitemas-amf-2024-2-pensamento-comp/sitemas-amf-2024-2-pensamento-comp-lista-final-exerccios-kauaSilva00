# Lista para armazenar as tarefas
tarefas = []

def adicionar_tarefa(tarefa):
    """Adiciona uma tarefa à lista."""
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def visualizar_tarefas():
    """Exibe todas as tarefas na lista."""
    if tarefas:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
    else:
        print("Não há tarefas na lista.")

def remover_tarefa(indice):
    """Remove uma tarefa da lista pelo índice (base 0)."""
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido. Nenhuma tarefa foi removida.")

def menu():
    """Função para exibir o menu e interagir com o usuário."""
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(tarefa)
        elif escolha == "2":
            visualizar_tarefas()
        elif escolha == "3":
            visualizar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                remover_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif escolha == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

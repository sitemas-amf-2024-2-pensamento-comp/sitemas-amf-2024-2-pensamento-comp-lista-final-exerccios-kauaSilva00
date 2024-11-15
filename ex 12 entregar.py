# Criando uma lista de exemplo
lista = [10, 20, 30, 40, 50, 20]

# Demonstração do pop() - removendo o último item (sem índice)
ultimo_item = lista.pop()
print("Lista após pop():", lista)
print("Último item removido:", ultimo_item)

# Demonstração do pop() com índice - removendo o item no índice 2
item_no_indice_2 = lista.pop(2)
print("Lista após pop(2):", lista)
print("Item removido no índice 2:", item_no_indice_2)

# Demonstração do remove() - removendo o valor 20
lista.remove(20)
print("Lista após remove(20):", lista)

# Tentando remover um valor que não existe (isso gera um e

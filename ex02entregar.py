inteiro = 10        # Tipo 'int'
flutuante = 3.14    # Tipo 'float'
texto = "Python"    # Tipo 'str'
booleano = True     # Tipo 'bool'

# Exibindo as variáveis e seus tipos
print("Variável inteiro:", inteiro, "| Tipo:", type(inteiro))
print("Variável flutuante:", flutuante, "| Tipo:", type(flutuante))
print("Variável texto:", texto, "| Tipo:", type(texto))
print("Variável booleano:", booleano, "| Tipo:", type(booleano))

# Operações com diferentes tipos de variáveis

# Operação com inteiros
soma = inteiro + 5
print("\nSoma de inteiro com 5:", soma)

# Operação com floats
multiplicacao = flutuante * 2
print("Multiplicação de flutuante por 2:", multiplicacao)

# Concatenando strings
mensagem = texto + " é incrível!"
print("Mensagem concatenada:", mensagem)

# Usando booleanos em uma condição
if booleano:
    print("O valor booleano é Verdadeiro.")
else:
    print("O valor booleano é Falso.")
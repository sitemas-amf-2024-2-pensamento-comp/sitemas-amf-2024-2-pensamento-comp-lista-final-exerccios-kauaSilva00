# Lista de números de 1 a 10
numeros = list(range(1, 11))

# Usando o loop while
i = 0
while i < len(numeros):
    numero = numeros[i]
    print(f"O quadrado de {numero} é {numero ** 2}")
    i += 1

# Lista de números de 1 a 10
numeros = list(range(1, 11))

# Usando o loop for
for numero in numeros:
    print(f"O quadrado de {numero} é {numero ** 2}")

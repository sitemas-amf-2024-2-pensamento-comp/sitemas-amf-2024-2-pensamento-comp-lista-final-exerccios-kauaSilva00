
def listar_impares_ate_100():
    impares = []
    for i in range(1, 101):
        if i % 2 != 0:  # Verifica se o número é ímpar
            impares.append(i)
    return impares

# Testando a função
impares = listar_impares_ate_100()
print("Números ímpares de 1 até 100:", impares)

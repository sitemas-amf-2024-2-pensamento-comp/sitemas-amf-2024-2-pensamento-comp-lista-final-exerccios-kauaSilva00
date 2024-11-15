# Função para calcular a média de dois números
def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamando a função e exibindo o resultado
resultado = calcular_media(numero1, numero2)
print(f"A média de {numero1} e {numero2} é {resultado:.2f}")

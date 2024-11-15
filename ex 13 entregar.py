# Iterando de 1 a 10
for numero in range(1, 11):
    if numero == 5:
        print(f"Encontrado o número 5. Saindo do laço.")
        break  # Para o loop quando o número for 5
    elif numero == 3:
        print(f"Pulando o número 3.")
        continue  # Pula o número 3 e vai para a próxima iteração
    print(f"Numero atual: {numero}")

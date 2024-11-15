import random

def adivinhar_numero():
    # Gerando um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    
    # Instruções iniciais
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 100.")
    
    tentativas = 0  # Contador de tentativas
    
    while True:
        
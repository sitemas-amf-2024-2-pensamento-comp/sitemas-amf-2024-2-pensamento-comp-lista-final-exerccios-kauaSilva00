def calcular_renda_liquida(renda, despesas):
    """Calcula a renda líquida subtraindo as despesas mensais da renda."""
    return renda - despesas

def verificar_eligibilidade(renda_liquida, pontuacao_credito, parcela_emprestimo):
    """Verifica a elegibilidade para o empréstimo com base na renda líquida, pontuação de crédito e parcela mensal."""
    # Definindo os critérios
    pontuacao_minima = 600
    limite_parcela = 0.30 * renda_liquida  # 30% da renda líquida
    
    if pontuacao_credito >= pontuacao_minima and parcela_emprestimo <= limite_parcela:
        return True
    else:
        return False

def main():
    # Leitura dos dados do cliente
    renda = float(input("Digite a sua renda mensal: R$ "))
    despesas = float(input("Digite suas despesas mensais: R$ "))
    pontuacao_credito = int(input("Digite sua pontuação de crédito: "))
    parcela_emprestimo = float(input("Digite o valor da parcela do empré



# Imprimindo a tabela de resultados
print(f"{'A':<5}{'B':<5}{'C':<5}{'A || (B && C)':<20}{'!A && B && C':<20}{'!(A && B && !C)':<20}")
print("-" * 70)

for A, B, C in combinations:
    res_1 = expr_1(A, B, C)
    res_2 = expr_2(A, B, C)
    res_3 = expr_3(A, B, C)
    print(f"{A:<5}{B:<5}{C:<5}{res_1:<20}{res_2:<20}{res_3:<20}")



        # Funções para as expressões booleanas
def expr_1(A, B, C):
    return A or (B and C)

def expr_2(A, B, C):
    return (not A) and B and C

def expr_3(A, B, C):
    return not (A and B and not C)

# Testando todas as combinações de A, B e C
combinations = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False)
]

# Imprimindo a tabela de resultados
print(f"{'A':<5}{'B':<5}{'C':<5}{'A || (B && C)':<20}{'!A && B && C':<20}{'!(A && B && !C)':<20}")
print("-" * 70)

for A, B, C in combinations:
    res_1 = expr_1(A, B, C)
    res_2 = expr_2(A, B, C)
    res_3 = expr_3(A, B, C)
    print(f"{A:<5}{B:<5}{C:<5}{res_1:<20}{res_2:<20}{res_3:<20}")

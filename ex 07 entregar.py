# Função para calcular a tabela verdade
def tabela_verdade():
    print("P (Chuva) | Q (Sol) | R (Avaliação G1) | P ∨ Q (Chuva ou Sol) | R ↔ (P ∨ Q)")
    print("-" * 70)
    
    # Variáveis P, Q e R
    for P in [True, False]:
        for Q in [True, False]:
            for R in [True, False]:
                # P ∨ Q
                p_ou_q = P or Q
                # R ↔ (P ∨ Q)
                r_bicondicional = (R == p_ou_q)
                
                # Imprimindo a linha da tabela verdade
                print(f"{P:9} | {Q:7} | {R:15} | {p_ou_q:18} | {r_bicondicional:12}")

# Chama a função para gerar a tabela verdade
tabela_verdade()

P (Chuva) | Q (Sol) | R (Avaliação G1) | P ∨ Q (Chuva ou Sol) | R ↔ (P ∨ Q)
----------------------------------------------------------------------
True      | True    | True             | True                | True        
True      | True    | False            | True                | False       
True      | False   | True             | True                | True        
True      | False   | False            | True                | False       
False     | True    | True             | True                | True        
False     | True    | False            | True                | False       
False     | False   | True             | False               | False       
False     | False   | False            | False               | True        

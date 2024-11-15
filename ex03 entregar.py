# Variáveis de exemplo
a = 10
b = 20
x = True
y = False

# 1. Menor que (<)
if a < b:
    print(f"{a} é menor que {b}")

# 2. Atribuição (=)
# (O operador '=' é usado para atribuição e não é parte da comparação em uma condição. Exemplo:
x = 5  # Atribuindo 5 à variável x
print(f"x agora é: {x}")

# 3. Maior ou igual a (>=)
if b >= a:
    print(f"{b} é maior ou igual a {a}")

# 4. Diferente de (!=)
if a != b:
    print(f"{a} é diferente de {b}")

# 5. Menor ou igual a (<=)
if a <= b:
    print(f"{a} é menor ou igual a {b}")

# 6. NOT (Não)
if not x:
    print("x é False")
else:
    print("x é True")  # Porque x foi atribuído a True no exemplo

# 7. AND (E)
if x and y:
    print("Ambos são True")
else:
    print("Pelo menos um é False")  # Como y é False, esse bloco será executado

# 8. Maior que (>)
if b > a:
    print(f"{b} é maior que {a}")

# 9. Igual a (==)
if a == 10:
    print(f"{a} é igual a 10")

# 10. OR (Ou)
if x or y:
    print("Pelo menos um dos valores é True")  # Como x é True, este bloco será executado
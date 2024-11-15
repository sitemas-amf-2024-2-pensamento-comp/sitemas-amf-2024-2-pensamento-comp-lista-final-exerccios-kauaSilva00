def classificar_pessoa(idade, sexo):
    # Classificação de idade
    if idade < 18:
        classificacao = "menor de idade"
    elif idade >= 18 and idade <= 60:
        classificacao = "adulto"
    else:
        classificacao = "idoso"

    # Adicionar detalhes com base no sexo
    if sexo.lower() == 'masculino':
        saudacao = "Homem"
    elif sexo.lower() == 'feminino':
        saudacao = "Mulher"
    else:
        saudacao = "Pessoa"

    # Exibindo o resultado
    print(f"{saudacao} com {idade} anos é classificado como {classificacao}.")

# Exemplos de uso da função
classificar_pessoa(17, 'masculino')  # Exemplo de menor de idade
classificar_pessoa(25, 'feminino')  # Exemplo de adulto
classificar_pessoa(70, 'masculino')  # Exemplo de idoso
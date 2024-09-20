def calcular_rank(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldo_vitorias = vitorias - derrotas

    # Classificação por vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # Retorna a mensagem final
    return f"O Herói tem de saldo {saldo_vitorias} e está no nível de {nivel}"

# Teste da função
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

resultado = calcular_rank(vitorias, derrotas)
print(resultado)

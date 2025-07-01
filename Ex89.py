notas = {
    "50": 0,
    "20": 0,
    "10": 0,
    "2": 0,
    "1": 0
}

while True:
    try:
        value = int(input("Qual valor você quer sacar? R$"))
        if value <= 0:
            raise ValueError("Digite um valor válido...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

denominacoes = [50, 20, 10, 2, 1]

for nota_valor in denominacoes:
    while value >= nota_valor:
        value -= nota_valor
        notas[str(nota_valor)] += 1

for nota_str, quantidade in notas.items():
    if quantidade > 0:
        print(f"{quantidade} notas de R${nota_str},00")
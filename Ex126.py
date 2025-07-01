import Assets.functions as fn

real = float(input("Quantos reais você tem na conta? R$"))

while True:
    try:
        pergunta = int(input("Quer converter seu dinheiro para qual moeda?\n\n[1] Dólar\n[2] Euro\n[3] Iene\n\nR: "))

        if pergunta not in {1,2,3}:
            raise ValueError("Você deve escolher uma das opções...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

match pergunta:
    case 1:
        valor_convertido, nome_moeda = fn.real_to_dolar(real)
    case 2:
        valor_convertido, nome_moeda = fn.real_to_euro(real)
    case 3:
        valor_convertido, nome_moeda = fn.real_to_iene(real)

print(f"A conversão do seu dinheiro de real para {nome_moeda} ficou em {valor_convertido:.2f}")
valor = float(input("Qual foi o valor da compra? R$"))

while True:
    try:
        resposta = int(input(f"Quer pagar sua compra de R${valor} em que modalidade:\n\n[1] À vista ou PIX\n[2] Cartão de Débito\n[3] Cartão de Crédito\n\nR: "))

        if resposta not in {1, 2, 3}:
            raise ValueError("Você deve escolher uma das opções...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

valor_final = valor
div = 1
match resposta:
    case 1:
        valor_final -= valor_final * 0.1
    case 2:
        valor_final -= valor_final * 0.05
    case 3:
        while True:
            try:
                div = int(input("Quer dividir em quantas vezes? x"))

                if div <= 0:
                    raise ValueError("O valor não pode ser 0 nem negativo...")
                break
            except ValueError as e:
                print(f"\nErro: {e}\n")
        
        if div <= 3:
            valor_final += valor_final * 0.05
        else:
            valor_final += valor_final * 0.1

parcelas = valor_final / div

print(f"Sua compra de {valor} parcelada em x{div} de R${parcelas} sendo um total de R${valor_final}.")
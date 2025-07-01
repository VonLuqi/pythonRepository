soma_compras = []

while True:
    soma_compras.append(float(input("\nDigite o valor do produto: R$")))

    parar = input("\nQuer parar? [s/n] ").strip().lower()

    if parar in {'s','sim','y','yes'}: break

while True:
    try:
        modal = (int(input("Qual será a forma de pagamento?\n\n[1] À vista\n[2] Boleto\n[3] Débito\n\nR: ")))

        if modal not in {1,2,3}:
            raise ValueError("Você deve escolher uma das opções...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

print("===== VALOR A SER PAGO =====\n")

print(*soma_compras,sep=" + ",end="")

soma = sum(soma_compras)
valor_final = soma

match modal:
    case 1:
        valor_final = soma * 0.9
    case 2:
        valor_final = soma * 1.1
    case 3:
        valor_final = soma * 0.95

print(" = R${:.2f} e com o modificador do pagamento ficou em R${:.2f}".format(soma,valor_final),end="")
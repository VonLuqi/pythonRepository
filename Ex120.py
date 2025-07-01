import Assets.functions as fn

valor = float(input("Qual o valor da compra? R$"))

while True:
    try:
        modal = int(input("Em qual modalidade deseja pagar?\n\n[1] À vista\n[2] À prazo\n[3] No cartão\n\nR: "))

        if modal not in {1,2,3}:
            raise ValueError("Você deve escolher alguma das opções.")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

total = 0

match modal:
    case 1:
        total = fn.a_vista(valor)
    case 2:
        total = fn.a_prazo(valor)
    case 3:
        total = fn.cartao(valor)

if modal in {1,2}:
    print(f"O valor final de sua compra ficou em R${total}")
else:
    print(f"Suas parcelas ficaram em R${total}")
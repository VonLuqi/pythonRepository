import Assets.functions as fn

while True:
    try:
        escolha = input("Quer abastecer com qual combustível?\n\n[A] Álcool\n[G] Gasolina\n\nR: ")

        if escolha not in {'a','A','g','G'}:
            raise ValueError("Você deve escolher [A] ou [G]...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")
litros = float(input("Quer colocar quantos litros? "))

total_a_pagar = fn.abastecer(litros, escolha)

print(f"Você deve pagar R${total_a_pagar:.2f}.")
padrao_a = 0
padrao_b = 0
padrao_c = 0

for i in range(4):
    while True:
        try:
            name = input(f"Digite o nome da venda: ")
            value = float(input(f"Digite o valor da venda '{name}': "))

            if value <= 0:
                raise ValueError("Não é válido valores negativos...")
            if value <= 499.99: padrao_c += 1
            elif value <= 999.99: padrao_b += 1
            else: padrao_a += 1
            break
        except ValueError as e:
            print(f"\nErro: {e}\n")

print(f"Clientes de padrão A: {padrao_a}\nClientes de padrão B: {padrao_b}\nClientes de padrão C: {padrao_c}")
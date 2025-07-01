carrinho_compras = []

while True:
    carrinho_compras.append(str(input("\nQual produto você quer pôr no carrinho? ")))

    parar = input("\nQuer parar? [s/n] ").strip().lower()

    if parar in {'s','sim','y','yes'}: break

print("===== CARRINHO DE COMPRAS =====\n")

for compras in carrinho_compras:
    print(compras)
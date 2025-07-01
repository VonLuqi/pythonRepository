soma_compras = []

while True:
    soma_compras.append(float(input("\nDigite o valor do produto: R$")))

    parar = input("\nQuer parar? [s/n] ").strip().lower()

    if parar in {'s','sim','y','yes'}: break

print("===== VALOR A SER PAGO =====\n")

print(*soma_compras,sep=" + ",end="")

soma = sum(soma_compras)

print(" = R${}".format(soma),end="")
compra = float(input("Digite o valor da compra: R$"))

if compra > 500: compra = compra - (compra * 0.05)

print(f"O valor final da sua compra é R${compra}")
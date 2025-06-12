compras = [
    float(input("Qual o valor da primeira compra? ")),
    float(input("Qual o valor da segunda compra? ")),
    float(input("Qual o valor da terceira compra? "))
]

soma = compras[0] + compras[1] + compras[2]
media = soma / 3

msn = "verdadeiro" if soma > media * 2 else "falso"
print(msn)
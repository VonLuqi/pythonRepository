num = [
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: "))
]

operacao = input("Qual operação quer fazer? (soma | media) ")
calc = num[0] + num[1] if operacao == "soma" else (num[0] + num[1]) / 2

print(f"{operacao} de {num[0]} e {num[1]} é igual a {calc}!\n")
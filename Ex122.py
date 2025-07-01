import Assets.functions as fn

valor = int(input("Digite um número: "))

valor_dobrado = fn.dobrar(valor)

novo_valor = int(input("Digite um novo número: "))

print(valor_dobrado + novo_valor)
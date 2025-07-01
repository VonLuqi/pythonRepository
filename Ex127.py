import Assets.functions as fn

km_percorrido = float(input("Quantos km você andou com o carro alugado? "))
dias = int(input("E quantos dias você alugou? "))

total_valor = fn.cobrar(km_percorrido, dias)

print(f"Seu aluguel ficou em R${total_valor}.")
area_pintura = float(input("Digite o valor em metros quadrados dos lugares que serão pintados: "))

litros_tinta = area_pintura / 3

latas = 0

while litros_tinta >= 18: 
    latas += 1
    litros_tinta -= 18

if litros_tinta > 0.0: latas += 1

preco = latas * 80

print(f"Você vai precisar de {latas} latas de tinta para pintar a área que forneceu, e para isso terá que desembolsar R${preco}.")
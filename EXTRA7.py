def Get_latas_18(litros: float):
    latas = 0

    while litros >= 18: 
        latas += 1
        litros -= 18

    value = latas * 80

    return latas, value, litros

def Get_latas_36(litros: float):
    latas = 0

    while litros >= 3.6: 
        latas += 1
        litros -= 3.6

    value = latas * 25

    return latas, value, litros


def Get_optimized_latas(litros: float):

    latas_18, value_latas_18, litros_restantes = Get_latas_18(litros)

    latas_36, value_latas_36, litros_restantes = Get_latas_36(litros_restantes)

    if litros_restantes > 0:
        latas_36 += 1
        value_latas_36 += 25

    return latas_18, value_latas_18, latas_36, value_latas_36


area_pintura = float(input("Digite o valor em metros quadrados dos lugares que serão pintados: "))

litros_tinta = area_pintura / 6

latas_only_18, value_only_18, l = Get_latas_18(litros_tinta)

if l > 0: 
    latas_only_18 += 1
    value_only_18 += 80

latas_only_36, value_only_36, l = Get_latas_36(litros_tinta)

if l > 0: 
    latas_only_36 += 1
    value_only_36 += 25

Latas_optimized_18, value_optimized_18, Latas_optimized_36, value_optimized_36 = Get_optimized_latas(litros_tinta)

print(f"\nComprando apenas galões de 18 litros, você vai precisar de {latas_only_18} e vai pagar R${value_only_18}"
      f"\nJá se estiver comprando apenas Latas de 3,6 litros, você vai precisar de {latas_only_36} e vai pagar R${value_only_36}"
      f"\nE caso queira o modo mais otimizado, irá precisar de {Latas_optimized_18} latas de 18 litros e {Latas_optimized_36} latas de 3,6 litros, pagando no total R${value_optimized_18 + value_optimized_36}.")

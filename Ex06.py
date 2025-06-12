import os

os.system('cls')

peso = float(input("Digite seu peso atual:\n\nKg: "))
qntSanduiche = int(input("\nE quantos sanduíches você comeu?\n\nQnt: "))

os.system('cls')

novoPeso = (qntSanduiche * 0.1) + peso
gasto = qntSanduiche * 8.5

print(f"Seu novo peso depois desses sanduíches é de {novoPeso:.1f} Kg e você gastou aproximadamnete R${gasto:.2f} com sanduíches esse mês!\n")

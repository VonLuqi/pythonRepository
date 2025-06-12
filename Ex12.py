import os

os.system('cls')

saldo = float(input("Quanto de dinheiro você tem?\n\nR$"))
compra = float(input("\nQuanto está a compra do mês?\n\nR$"))

os.system('cls')

pagamento = "Tem dinheiro!\n" if saldo >= compra else "Não tem dinheiro!\n"

print(pagamento)
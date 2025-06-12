import os

os.system('cls')

preco = float(input("Qual o preço do produto?\n\nR$"))
desconto = int(input("\nE qual o desconto? (%)\n\nR: "))

os.system('cls')

precoFinal = preco - (preco * (desconto / 100))

print(f"O produto custava R${preco:.2f} mas teve desconto de {desconto}% por isso agora esta custando {precoFinal:.2f} reais!\n")

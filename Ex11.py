import os

os.system('cls')

cel = float(input("Digite a temperatura atual em Celcius:\n\nR: "))
fah = ((9 * cel) / 5) + 32

os.system('cls')

print(f"A temperatura atual em Fahrenheit é {fah}!\n")
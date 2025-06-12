n = [int(input(f"Digit o número de número {i+1}: ")) for i in range(3)]

pares, impares = 0, 0

for numero in n:
    if numero % 2 == 0: pares += numero
    else: impares += numero
    
print(f"A soma dos números pares é {pares} e a soma dos números ímpares é {impares}!\n")
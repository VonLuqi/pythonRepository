n = [int(input(f"Digite o número de número {i+1}: ")) for i in range(4)]

somaP = 0
pares = 0
maiorP = 0

for num in n:
    if num % 2 == 0:
        somaP += num
        pares += 1
        if num > maiorP: maiorP = num
        
print(f"Foram digitados {pares} números pares\nA soma desses números pares é {somaP}\nO maior número par é {maiorP}\n")
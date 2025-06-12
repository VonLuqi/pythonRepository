n = 0
sumP = 0
sumI = 0

c = 0

while c in range(5):
    c += 1
    n = int(input("Digite um número: "))
    if n % 2 == 0: sumP += n
    else: sumI += n
    
print(f"A soma dos ímpares é {sumI} e a soma dos pares é {sumP}")
mult5 = 0
mult3 = 0

c = 0

while c in range(7):
    c += 1
    n = int(input("Digite um número: "))
    if n % 5 == 0: mult5 += 1
    if n % 3 == 0: mult3 += 1
    
print(f"Foram identificados {mult5} números que são múltiplos de cinco e {mult3} números que são múltiplos por 3.")
soma = 0
c = 0

while True:
    n = int(input(f"Digite o n{c+1}: "))
    
    if n == 999: break

    c += 1
    soma += n
    
print(f"Foram digitados {c} números e a soma deles é {soma}")
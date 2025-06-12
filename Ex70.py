n = []

c = 0

menor_26 = 0
menor_51 = 0
menor_76 = 0
menor_101 = 0

while True:
    numero_digitado = int(input(f"Digite o n{c+1}: "))
    n.append(numero_digitado)
    
    c += 1
    
    if numero_digitado < 26: menor_26 += 1
    elif numero_digitado < 51: menor_51 += 1
    elif numero_digitado < 76: menor_76 += 1
    elif numero_digitado < 101: menor_101 += 1
        
    continuar = input("Você quer continuar? [S/N] ").strip().lower()
    if continuar not in ['s', 'sim', 'yes', 'y']: break
    
print(f"\nNúmeros entre [0-25]: {menor_26}\nNúmeros entre [26-50]: {menor_51}\nNúmeros entre [51-75]: {menor_76}\nNúmeros entre [76-100]: {menor_101}")
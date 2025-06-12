n = []

c = 0
valores_positivos = 0
quantidade_negativos = 0
media_positivos = 0

while True:
    numero_digitado = int(input(f"Digite o n{c+1}: "))
    n.append(numero_digitado)
    
    if numero_digitado > 0:
        valores_positivos += 1
        media_positivos += numero_digitado
    else: quantidade_negativos += 1
    
    c += 1
    
    continuar = input("Você quer continuar? [S/N] ").strip().lower()
    if continuar not in ['s', 'sim', 'yes', 'y']: break

if valores_positivos > 0: media_positivos /= len(n)

print(f"Valores positivos inseridos: {valores_positivos}\nValores negativos inseridos: {quantidade_negativos}\nMédia dos valores positivos: {media_positivos}")
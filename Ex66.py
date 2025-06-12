pesoMedio = 70
pesoAcima = 0
pesoAbaixo = 0

c = 0

while c in range(4):
    c += 1
    peso = float(input("Qual o seu peso? "))
    if peso > pesoMedio: pesoAcima += 1
    else: pesoAbaixo += 1
    
print(f"Existe {pesoAcima} pessoas que estão acima do peso médio e existe {pesoAbaixo} pessoas com peso igual ou abaixo a média.")
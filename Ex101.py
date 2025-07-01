notas = [float(input(f"Digite a sua nota {i+1}: ")) for i in range(6)]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f"\nNotas acima da média: ({media})")

for nota in notas: 
    if nota > media: print(f"{nota:.1f}")

print(f"\nA maior nota é: {maior}\nE a menor é: {menor}")
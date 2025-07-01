valores = [int(input(f"Digite o {i+1}° valor: ")) for i in range(4)]

qnt_nine = 0

for val in valores:
    if val == 9: qnt_nine += 1

print(f"Apareceram {qnt_nine} números 9.")
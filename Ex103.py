valores = [int(input(f"Digite o {i+1}° valor: ")) for i in range(3)]

qnt_fourteen = 0

for val in valores:
    if val == 9: qnt_fourteen += 1

print(f"Apareceram {qnt_fourteen} números 9.")
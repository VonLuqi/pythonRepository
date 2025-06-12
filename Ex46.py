idade = [int(input(f"Qual a sua idade pessoa {i+1}? ")) for i in range(2)]
categoria = []

for i in idade:
    if i <= 9: categoria.append("mirim")
    if 10 <= i <= 14: categoria.append("infantil")
    if 15 <= i <= 18: categoria.append("jovem")
    if 19 <= i <= 24: categoria.append("adulto")
    
if idade[0] == idade[1]:
    hr = input("Qual será o horário da luta? ")
    print(f"Está marcado a luta de uma pessoa com {idade[0]} anos e outra pessoa com {idade[1]} anos na hora {hr}")
else: print("Luta cancelada")
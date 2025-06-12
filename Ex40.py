prof = {
    "valH": float(input("Digite suas informações:\n\nValor da Hora Aula: R$")),
    "numA": int(input("Números de Aulas Lecionadas: ")),
}

salario_bruto = prof["valH"] * prof["numA"]
inss = 0

if salario_bruto <= 1518: inss = salario_bruto * 0.075
if 1518.01 <= salario_bruto <= 2793.88: inss = salario_bruto * 0.09
if 2793.89 <= salario_bruto <= 4190.83: inss = salario_bruto * 0.12
if 4190.84 <= salario_bruto <= 8157.41: inss = salario_bruto * 0.12

salario_liquido = salario_bruto - inss

print(f"Seu salário ficou em R${salario_bruto:.2f}, porém com as deduções do INSS ficou em R${salario_liquido:.2f}!\n")
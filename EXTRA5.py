valor_hora = float(input("Quanto você ganha por hora? "))
horas = int(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas
imposto_renda = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto_renda - INSS - sindicato

print(f"Seu salário bruto é {salario_bruto}, com os descontos de imposto de renda (R${imposto_renda}), INSS (R${INSS}) e sindicato (R${sindicato}), seu salário líquido ficou em R${salario_liquido}.")
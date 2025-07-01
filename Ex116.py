import Assets.functions as fn

salario = float(input("Digite seu salário: R$"))

total = fn.ferias(salario)

print(f"Você receberá no total {total} que inclui o salario do mês mais as suas ferias")
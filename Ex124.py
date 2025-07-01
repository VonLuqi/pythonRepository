import Assets.functions as fn

cargo = input("Qual o seu cargo? ")

salario = fn.analisar_cargo(cargo.strip().lower()) * 12

print(f"O seu salário como {cargo} é R${salario}")
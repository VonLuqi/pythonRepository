time = input("Qual time você torce? ").lower().strip()

model = 0

if time in ["atletico","cruzeiro"]: model = int(input("Você prefere o [1 - modelo 1] ou [2 - modelo 2]? "))
if time == "atletico": print("o valor será de R$85.00" if model == 1 else "o valor será de R$75.00")
if time == "cruzeiro": print("o valor será de R$45.00" if model == 1 else "o valor será de R$95.00")
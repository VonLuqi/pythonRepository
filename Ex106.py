import random as r

positions = [(r.randint(1, 50)) for i in range(4)]

random = positions[r.randint(0,3)]

n = int(input("Qual número está procurando? "))
sum_num = random

if n == random: 
    sum_num += n
    print(f"Você achou o número, que era {random}, e sua soma ficou em {sum_num}")
else: print("Não achou o número")
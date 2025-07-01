import Assets.functions as fn
import random as r

random_vetor = [(r.randint(1, 100)) for i in range(4)]

val_3 = fn.analise_3(random_vetor[2])
val_2 = fn.analise_2(random_vetor[1])

final = (val_2 + val_3) * 3.14

print(final)
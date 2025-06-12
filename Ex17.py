import os
import time as t
import random as r

os.system('cls')

rand = r.randrange(1, 100)

msn = "deu certo" if rand > 17 and rand < 36 else "deu errado"
print(msn)
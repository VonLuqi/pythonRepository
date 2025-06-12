import os
import time as t

os.system('cls')

time = input("Qual o seu time de futebol favorito?\n\nR: ")

os.system('cls')

msn = "Time campeão!\n" if time == "araxa" else "Não sabe escolher time...\n"
print(msn)

t.sleep(2)
os.system('cls')

cidade = input("QUal a melhor cidade do Brasil?\n\nR: ")

os.system('cls')

msn = "Cidade boa!\n" if cidade != "sao paulo" else "Não sabe escolher cidade...\n"
print(msn)
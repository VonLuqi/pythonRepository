import os
import time as t

os.system('cls')

cond = input("O que te fez rico?\n\nR: ")

os.system('cls')

msn = "verdadeiro" if cond == ("nasci rico" or "nasci rica" or "casei" or "politica") else "falso"
print(msn)
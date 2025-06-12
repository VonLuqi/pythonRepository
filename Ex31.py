n = int(input("Digite um número: "))

if (n < 0): print("negativo não conta")
elif (n == 0): print("é zero")
else: print("é par" if n % 2 == 0 else "é ímpar")
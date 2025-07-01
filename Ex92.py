while True:
    try:
        num = int(input("Qual número quer descobrir se é primo? "))
        if num < 0:
            raise ValueError("Digite um valor válido...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

is_primo = True

if num <= 1:
    is_primo = False
elif num == 2:
    is_primo = True
else:
    if num % 2 == 0: is_primo = False
    else:
        div = 3
        while div * div <= num and is_primo:
            if num % div == 0:
                is_primo = False
            div += 2

print("é primo" if is_primo else "não é primo")
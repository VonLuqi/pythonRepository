sum_even = 0
qnt_even = 0

for i in range(6):
    num = int(input(f"Digite o n{i+1}: "))

    if num % 2 == 0: 
        sum_even += num
        qnt_even += 1

print(f"Foram digitados {qnt_even} números pares e sua soma é {sum_even}")
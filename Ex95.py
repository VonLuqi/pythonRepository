sum_nums = 0
while True:
    num = int(input("Digite um número: "))
    sum_nums += num

    if sum_nums > 1000:
        print(f"Excedeu em {sum_nums-1000}")
        break
    elif sum_nums == 1000:
        break
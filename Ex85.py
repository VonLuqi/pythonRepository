c = 0
sum_nums = 0

for i in range(9):
    num = int(input(f"Digite o n{i+1}: "))

    if num == 999: break

    c += 1
    sum_nums += num

print(f"Foram feitas {c} tentativas e a soma desses números é {sum_nums}!")
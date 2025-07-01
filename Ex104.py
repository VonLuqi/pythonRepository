nums = [int(input(f"Digite o n{i+1}: ")) for i in range(4)]

sum_even = 0

for num in nums:
    if num % 2 == 0: sum_even += num

print("Esses são todos os valores ímpares: ",end="")

odds = []

for num in nums:
    if num % 2 != 0: 
        print("{}".format(num),end=", ")
        odds.append(num)

print(f"\nA soma dos pares é: {sum_even}")
print(f"\n{odds}")
    
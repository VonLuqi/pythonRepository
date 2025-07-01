nums = [int(input(f"Digite o n{i+1}: ")) for i in range(4)]

sum_even = 0
evens = []
odds = []

for num in nums:
    if num % 2 == 0: 
        sum_even += num
        evens.append(num)
    else: odds.append(num)

print("\nÍmpares:\n")
print(*evens, sep=", ")
print("\nPares:\n")
print(*odds, sep=", ")
print(f"\nA soma dos pares é: {sum_even}")
import Assets.functions as fn

nums = [int(input(f"Digite o valor do n{i+1}: ")) for i in range(3)]

maior = fn.maior(nums)

print(f"O maior dos números é: {maior}")
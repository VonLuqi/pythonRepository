import Assets.functions as fn

nums = [int(input(f"Digite o valor do n{i+1}: ")) for i in range(2)]

maior = fn.maior(nums)
menor = fn.menor(nums)
media = fn.media([maior,menor])

print(f"O maior é {maior}, o menor é {menor} e a média deles é {media}")
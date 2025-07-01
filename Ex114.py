import Assets.functions as fn

nums = [int(input(f"Digite o valor do n{i+1}: ")) for i in range(2)]

while True:
    try:
        operacao = int(input("Você deseja fazer qual operação?\n\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n\nR: "))

        if operacao not in {1,2,3,4}:
            raise ValueError("Você deve escolher uma da opções")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

final = 0

match operacao:
    case 1:
        final = fn.soma(nums)
    case 2:
        final = fn.subtracao(nums[0],nums[1])
    case 3:
        final = fn.multiplicacao(nums)
    case 4:
        final = fn.divisao(nums[0],nums[1])
    
print(f"O resultado da sua operação foi: {final}")
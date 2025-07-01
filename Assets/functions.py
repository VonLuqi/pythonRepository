# Operações Matemáticas

def soma(nums):
    soma = 0
    
    for num in nums:
        soma += num

    return soma

def subtracao(a: int,b: int) -> int:
    return a - b

def multiplicacao(nums):
    divisao = 1

    for num in nums:
        divisao *= num

    return divisao

def divisao(a: int,b: int) -> float:
    return a / b

def dobrar(num):
    return num * 2

def media(nums):
    return soma(nums) / len(nums)

# Maior e Menor

def maior(nums):
    maior = 0

    for num in nums:
        if num > maior: maior = num

    return maior

def menor(nums):
    menor = float('inf')

    for num in nums:
        if num < menor: menor = num

    return menor

def analisar(nums):
    maior_valor = maior(nums)
    menor_valor = menor(nums)

    print(f"O maior dentre os números é {maior_valor}, e o menor {menor_valor}")


# funções variadas

def ferias(salario):
    ferias = salario * 1.33
    return ferias + salario

def cadastro(nome,sexo,idade):
    print(f"{nome} cadastrado com sucesso, com o sexo {sexo} e idade {idade}.")

def sucessor(num):
    return num + 1

def antecessor(num):
    return num - 1

def lascado():
    divida = float(input("Qual a sua dívida? R$"))
    tempo = int(input(f"Por quanto tempo (meses) você tem essa dívida de R${divida}: "))
    taxa = int(input("E qual a taxa (%) de juros para esse dívida? "))

    total = divida + (divida * tempo * (taxa / 100))
    return total

def analisar_cargo(cargo):
    if cargo in {'policial','medico'}: return 2000
    elif cargo in {'magico','coach'}: return 1500
    else: return 500

def analise_3(num):
    return num * 2

def analise_2(num):
    return num * 3

def investigar(respostas):
    resultado = "inocente"
    contador_de_envolvimento = 0
    for resposta in respostas:
        if resposta in {'s','sim','y','yes'}: contador_de_envolvimento += 1
    
    if contador_de_envolvimento == 2: resultado = "suspeito(a)"
    elif contador_de_envolvimento in {3,4}: resultado = "cúmplice"
    elif contador_de_envolvimento == 5: resultado = "assassino"

    return resultado

def abastecer(litros, escolha):
    valor_alcool = 1.9
    valor_gasolina = 2.5

    if escolha in {'a','A'}:
        total = litros * valor_alcool
        if litros <= 20:
            total_desconto = total - (total * 0.03)
        else:
            total_desconto = total - (total * 0.04)
    elif escolha in {'g','G'}:
        total = litros * valor_gasolina
        if litros <= 20:
            total_desconto = total - (total * 0.04)
        else:
            total_desconto = total - (total * 0.06)
        
    return total_desconto

def mostrar(nums):
    menor = min(nums)
    maior = max(nums)
    counter = menor

    for counter in range(menor, maior):
        if counter not in nums:
            print(counter)

def PouN(num):
    if num > 0: return 'P'
    elif num == 0: return 'O'
    else: return 'N'

def analise_par_ou_impar(num):
    if num % 2 == 0: return "par"
    else: return "ímpar"


# pagamento

def a_vista(valor):
    return valor * 0.9

def a_prazo(valor):
    return valor * 1.1

def cartao(valor):
    div = int(input("Quer dividir em quantas parcelas? "))
    return valor * 1.2 / div

def cobrar(km_percorrido, dias):
    return (60 * dias) + (0.15 * km_percorrido)

# conversores

def real_to_dolar(valor):
    return valor / 5.43, "dólar"

def real_to_euro(valor):
    return valor / 6.41, "euro"

def real_to_iene(valor):
    return valor * 26.45, "iene"
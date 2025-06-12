venda = float(input("Quanto você vendeu? R$"))

comissao = 0

if venda >= 22000:
    ano = int(input("Quantos anos você tem de empresa? "))
    if ano < 2: comissao = venda * 0.02
    if ano == 2: comissao = venda * 0.03
    if ano >= 3: comissao = venda * 0.04
    print(f"Sua comissão ficou em R${comissao}!")
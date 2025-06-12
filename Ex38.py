valor = float(input("Digite o valor do produto: R$"))
pag = int(input("Qual será a foram de pagamento?\n\n[1 - À Vista]\n[2 - À Vista no cartão]\n[3 - Parcelado no cartão]\n\nR: "))

div = 1
parcela = 0

if (pag == 1): valor -= valor * 0.15
if (pag == 2): valor -= valor * 0.1
if (pag == 3):
    div = int(input("\nQuer dividir em quantas vezes?\n\nR: "))
    valor += 0 if div <= 2 else valor * 0.1
parcela = valor / div
    
print(f"\nSeu produto de R${valor} ficou em {div}x de R${parcela} pela forma de pagamento!\n")
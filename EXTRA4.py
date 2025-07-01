peso_peixe = float(input("===== Sistema de Regulamento de Pesca =====\n\nPeso do Peixe: Kg"))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f"Seu peixe passou o regulamento em {excesso}Kg e sua multa devido ao ocorrido é de R${multa}.")
else: print("Seu peixe não passou o peso do regulamento.")
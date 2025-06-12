distancia = float(input("Qual a distância percorrida pelo Uber? (Km) "))

valor = 0.35 * distancia if distancia <= 200 else 0.2 * distancia

if input("O bairro de destino é perigoso? ").lower().strip() == "sim": valor = valor * 2 if distancia <= 200 else valor * 1.8

print(f"O valor final da corrida para o destino escolhido é {valor:.2f} reais!")
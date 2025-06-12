lados = [float(input(f"Digite o lado {i+1} do triângulo: ")) for i in range(3)]

maior_lado = max(lados)
somaM = sum(lados) - maior_lado

if maior_lado < somaM: print("É triângulo")
else: print("Não é triângulo")
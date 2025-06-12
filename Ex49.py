lados = [float(input(f"Digite o lado {i+1} do triângulo: ")) for i in range(3)]

maior_lado = max(lados)
somaM = sum(lados) - maior_lado

if maior_lado < somaM:
    print("É triângulo")
    if len(set(lados)) == 1: print("É equilátero")
    if len(set(lados)) == 2: print("É isóceles")
    if len(set(lados)) == 3: print("É escaleno")
else: print("Não é triângulo")
nums = {
    "inteiro": [int(input(f"Digite o {i+1} num inteiro: ")) for i in range(2)],
    "real": float(input("Digite um número real: "))
}

produto = (nums["inteiro"][0] * 2) * (nums["inteiro"][1] / 2)
soma = (nums["inteiro"][0] * 3) + nums["real"]
cubo = nums["real"] ** 3

print(f"Produto: {produto}\nSoma: {soma}\nAo Cubo: {cubo}")
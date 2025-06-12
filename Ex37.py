aluno = {
    "nome": input("Digite seu nome: "),
    "notas": [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]
}

soma = sum(aluno["notas"])
media = soma / len(aluno["notas"])

print(f"{aluno['nome']} foi aprovado!\n" if media >= 7 else f"{aluno['nome']} foi reprovado!\n")
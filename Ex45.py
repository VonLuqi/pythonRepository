aluno = {
    "notas": [float(input(f"Qual a nota {i+1}: (0 a 100) ")) for i in range(2)],
    "frequencia": int(input("Qual a sua frequência nas aulas? (%) "))
}

media = sum(aluno["notas"]) / len(aluno["notas"])

if media >= 60 and aluno["frequencia"] > 75: print("aprovado")
elif 40 <= media < 60:
    print("recuperação")
    rec = float(input("Qual a sua nota de recuperação? (0 a 100) "))
    if rec <= 69.99: print("reprovado")
    else: print("aprovado")
else: print("reprovado sem direito a recuperação")
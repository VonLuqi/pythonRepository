# Crie um sistema em que temos um vetor que armazenará "times" de futebol. Esse vetor deve ser declarado com 2 times. Em seguida faça um looping que rode a quantidade de parâmetros dentro do vetor usando (for i in vetor), e dentro do looping você deve perguntar um novo time para o usuário e adicioná-lo ao vetor. Faça com que quando o vetor tiver 4 parâmetros pare o programa.

time = ["atletico","cruzeiro"]

for i in time:
    time.append(str(input("Digite um novo time: ")))
    if len(time) == 4: break

print(time)
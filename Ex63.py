init = int(input("Qual número quer começar a contagem? "))
end = int(input("QUal será o valor final da contagem? "))
jump = int(input("Quer pular a contagem de quantos em quantos? "))

c = init

while c <= end:
    print(c)
    c += jump
r = int(input("Seu conhecimento de Excel é? [1] básico [2] intermediário [3] avançado: "))

match r:
    case 1:
        op = input("Qual fórmula quer saber mais? [1] SOMA [2] MÉDIA [3] MÁXIMO: ")
        if op == 1: print("ela soma")
        if op == 2: print("ela tira média")
        if op == 2: print("ela retorna o maior número")
    case 2:
        op = input("Qual fórmula quer saber mais? [1] SE [2] SOMASE [3] CONT.SE: ")
        if op == 1: print("ele compara lógicas")
        if op == 2: print("ela soma caso algo aconteça")
        if op == 2: print("ele conta quanto de algo tem em uma tabela")
    case 3:
        op = input("Qual fórmula quer saber mais? [1] ORDEM.EQ [2] PROCV [3] PROCH: ")
        if op == 1: print("retorna a posição de um número em uma lista de números")
        if op == 2: print("é usada para procurar um valor em uma coluna e, em seguida, retornar um valor correspondente de outra coluna na mesma linha")
        if op == 2: print("Ela busca um valor específico na primeira linha de uma tabela e retorna um valor correspondente de uma linha específica (indicada pelo índice)")
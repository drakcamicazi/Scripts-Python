def hashing_function(word, listsize): #Dado uma string, a função hashing aloca a posição na lista.

        sum = 0
        for i in range(len(word)):
            sum = sum + ord(word[i])

        return sum%listsize

list = []

listsize = int(input('Entre com o numero de palavras que deseja alocar: '))

for j in range(listsize):
    word = input('Entre com uma palavra a ser alocada: ')
    alocation = hashing_function(word, listsize)
    list.insert(alocation,word) #Insere os elementos na lista, já com a posição da função hashing.

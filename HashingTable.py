def hashing_function(word, tablesize):

        sum = 0
        for i in range(len(word)):
            sum = sum + ord(word[i])

        return sum%tablesize



palavra = []

tablesize = int(input('Entre com o numero de palavras que deseja alocar: '))

for j in range(tablesize):
    word = input('Entre com uma palavra a ser alocada: ')
    alocation = hashing_function(word, tablesize)
    print(alocation)


for k in range(len(palavra)):
    print(palavra[k])


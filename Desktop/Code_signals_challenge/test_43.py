 # def isBeautifulString(inputString):

# s="akjsdhidb"
# k=sorted(s)
# # print(k)
# print(''.join(sorted(s)))

import string
def isBeautifulString(inputString):
    # Alphabet
    listaAlpha = list(string.ascii_lowercase)
    lista = sorted(list(inputString))
    contadores = [1]
    word = 0
    if lista[0] != 'a':
        return False
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            contadores[word] += 1
        else:
            # Is the next word consecutive in the alphabet?
            # index of previous letter
            indexes = listaAlpha.index(lista[i])
            if listaAlpha[indexes + 1] != lista[i + 1]:
                return False
            word += 1
            contadores.append(1)

    # print(contadores)
    for elem in range(len(contadores) - 1):
        if contadores[elem] < contadores[elem + 1]:
            return False
    return True
print(isBeautifulString("aabbb"))
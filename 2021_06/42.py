plik = open('DANE/napisy.txt').readlines()

haslo = ''
for i, x in enumerate(range(19, len(plik), 20)):
    haslo = haslo + plik[x][i]
print('Zadanie 4.2')
print(haslo)

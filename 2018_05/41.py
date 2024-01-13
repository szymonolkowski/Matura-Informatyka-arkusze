plik = open('Dane_PR/sygnaly.txt').readlines()

haslo = ''.join(plik[i][9] for i in range(39, len(plik), 40))
print('Zadanie 4.1')
print(haslo)

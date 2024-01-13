plik = open('DANE_2105/instrukcje.txt').readlines()


def dopisz(x):
    haslo.append(x)


def zmien(x):
    haslo.pop()
    haslo.append(x)


def usun():
    haslo.pop()


def przesun(x):
    pos = haslo.index(x)
    liczba = ord(x)
    ascii = chr(65) if liczba == 90 else chr(liczba+1)
    haslo[pos] = ascii


haslo = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    instrukcja = wiersz[0]
    litera = wiersz[1]
    if instrukcja == 'DOPISZ':
        dopisz(litera)
    elif instrukcja == 'PRZESUN':
        przesun(litera)

    elif instrukcja == 'USUN':
        usun()
    elif instrukcja == 'ZMIEN':
        zmien(litera)
haslo_cale = ''
for i in haslo:
    haslo_cale = haslo_cale + i

print('Zadanie 4.4')
print(haslo_cale)

plik = open('Dane_PR/liczby.txt').readlines()


def czyPotegaTrzy(num):
    while num % 3 == 0:
        num /= 3
    return num == 1


ile = 0
for wiersz in plik:
    wiersz = int(wiersz.strip())
    if czyPotegaTrzy(wiersz):
        ile += 1

print('Zadanie 4.1')
print(ile)

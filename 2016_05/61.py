plik = open('Dane_NOWA/dane_6_1.txt').readlines()


def szyfruj(slowo, klucz):
    klucz = klucz % 26
    return ''.join(
        chr(64 + abs(90 - ord(litera) - klucz))
        if ord(litera) + klucz > 90
        else chr(ord(litera) + klucz)
        for litera in slowo
    )


for wiersz in plik:
    wiersz = wiersz.strip()
    print(szyfruj(wiersz, 107))

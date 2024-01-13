plik = open('Dane_NOWA/dane_6_2.txt').readlines()


def odszyfruj(slowo, klucz):
    klucz = klucz % 26
    return ''.join(
        chr(91 + (ord(litera) - 65) - klucz)
        if ord(litera) - klucz < 65
        else chr(ord(litera) - klucz)
        for litera in slowo
    )


for wiersz in plik:
    wiersz = wiersz.strip().split()
    slowo = wiersz[0]
    klucz = int(wiersz[1])
    print(odszyfruj(slowo, klucz))

plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_nieparzyste = sum(
        int(wiersz[cyfra]) for cyfra in range(0, len(wiersz), 2)
    )
    suma_parzyste = sum(int(wiersz[cyfra]) for cyfra in range(1, len(wiersz), 2))
    cyfra_kontrolna = (suma_parzyste + suma_nieparzyste) % 10
    cyfra_kontrolna = 10 - cyfra_kontrolna
    cyfra_kontrolna = cyfra_kontrolna % 10
    print(cyfra_kontrolna, wiersz)

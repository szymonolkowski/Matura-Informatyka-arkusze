plik = open('Dane_PR2/pary.txt').readlines()


def isPrime(num):
    return False if num <= 1 else all(num % i != 0 for i in range(2, num))


print('Zadanie 4.1')
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    liczba = int(wiersz[0])
    for i in range(3, liczba):
        roznica = liczba - i
        if isPrime(i) and isPrime(roznica) and roznica != 2:
            if i < roznica:
                print(liczba, i, roznica)
            else:
                print(liczba, roznica, i)
            break

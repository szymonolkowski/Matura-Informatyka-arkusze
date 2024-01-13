plik = open('MIN-R2A1P-193_dane/liczby.txt').readlines()


def isPrime(x):
    return False if x <= 1 else all(x % i != 0 for i in range(2, x))


print('Zadanie 4.1')
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if int(wiersz) >= 100 and int(wiersz) <= 5000:
        if isPrime(int(wiersz)):
            print(wiersz)

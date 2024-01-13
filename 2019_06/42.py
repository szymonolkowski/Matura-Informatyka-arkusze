plik = open('MIN-R2A1P-193_dane/pierwsze.txt').readlines()


def isPrime(num):
    return all(num % i != 0 for i in range(2, num))


print('Zadanie 4.2')
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if isPrime(int(wiersz)) and isPrime(int(odbicie)):
        print(wiersz)

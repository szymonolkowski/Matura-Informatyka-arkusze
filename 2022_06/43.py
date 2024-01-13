plik = open('DANE/liczby.txt').readlines()


def isPrime(x):
    return False if x <= 1 else all(x % i != 0 for i in range(2, x))


pierwsze = []
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    wiersz = int(wiersz)
    odbicie = int(odbicie)
    if isPrime(wiersz) and isPrime(odbicie):
        pierwsze.append(wiersz)

print('Zadanie 4.3')
for i in pierwsze:
    print(i)

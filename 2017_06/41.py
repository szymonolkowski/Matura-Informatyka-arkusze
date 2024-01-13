plik = open('MIN-DANE-2017/punkty.txt').readlines()


def isPrime(num):
    return False if num <= 1 else all(num % i != 0 for i in range(2, num))


ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    if isPrime(x) and isPrime(y):
        ile += 1

print('Zadanie 4.1')
print(ile)

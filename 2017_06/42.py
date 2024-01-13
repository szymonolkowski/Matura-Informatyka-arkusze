plik = open('MIN-DANE-2017/punkty.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = wiersz[0]
    y = wiersz[1]
    set_x = set(x)
    set_y = set(y)
    if set_x == set_y:
        ile += 1

print('Zadanie 4.2')
print(ile)


b = "" #pusta

#pobieranie danych od uzytkownika
while True:
    a = input('Wprowadź liczbe: ')

    if a != '0':
        b += a
    else:
        pass

    if a == '0':
        break

#liczenie sumy i sredniej
sum = 0

for i in b:
    sum += int(i)
    sred = sum / (int(i) + 1)

#ile liczb wiekszych od sredniej

j = 0

for i in b:
    if int(i) > sred:
        j += 1
    else:
        pass

wybor = input('Wyświetl: \n1. Sume\n2. Srednia\n3. Liczby wieksze od sredniej\n4. Suma min max\nWybieram:\n')

match wybor:
    case '1':
        print(f'Suma: {sum}')
    case '2':
        print(f'Srednia: {sred}')
    case '3':
        print(f'Liczb większych od średniej: {j}')
    case '4':
        print(f'Suma min i max: {int(max(b)) + int(min(b))}')
        
while True:

    opcja = input('Wybieram:\n1. Zad3\n2. Zad4\n3. Wyjście\nWybieram:\n')

    match opcja:
        case '1':
            a = str(input('Podaj ciąg znaków: '))

            j = 0

            for i in a:
                if i != a or i != b:
                    j += 1

            print(f'Znaków różnych od "a" i "b" jest {j}')
        case '2':

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

        case '3':
            break
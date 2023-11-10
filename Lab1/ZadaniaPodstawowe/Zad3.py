print('\n3. Napisz program (zmodyfikuj z Lab0) działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć, dzielić oraz obliczać potęgę w zależności od potrzeb użytkownika.\n')

print('Jaką operację chcesz wykonać? \n1) dodawanie \n2) odejmowanie \n3) mnożenie \n4) dzielenie \n5) potęgowanie')

n = int(input('Wprowadź numer operacji: '))
a = int(input('Podaj argument 1: '))
b = int(input('Podaj argument 2: '))

match n:
    case 1:
        print(f'Wynik: {a} + {b} = {a + b}')
    case 2:
        print(f'Wynik: {a} - {b} = {a - b}')
    case 3:
        print(f'Wynik: {a} * {b} = {a * b}')
    case 4:
        print(f'Wynik: {a} / {b} = {a / b}')
    case 5:
        print(f'Wynik: {a} ** {b} = {a ** b}')

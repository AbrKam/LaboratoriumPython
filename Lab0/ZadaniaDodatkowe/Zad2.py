import math as m

print('\n2. Napisz program obliczający pole trójkąta o danych bokach\n')

a = int(input('Podaj pierwszy bok trójkąta (a): '))
b = int(input('Podaj drugi bok trójkąta (b): '))
c = int(input('Podaj trzeci bok trójkąta (c): '))

p = (a + b + c)/2

P = m.sqrt(p*(p - a)*(p - b)*(p - c))

print(f'\np wynosi {p}, P wynosi {P}\n')
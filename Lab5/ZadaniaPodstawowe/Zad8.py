import math as m

a = int(input('Podaj długość pierwszego boku "a": '))
b = int(input('Podaj długość drugiego boku "b": '))
kat = int(input('Podaj wartość kąta między tymi bokami: '))

if a < 0 or b < 0 or m.radians(kat) <= 0:
    print('Nieprawidłowe dane, trójkąt o takich parametrach nie istnieje')
elif (0.5 * a * b * m.sin(m.radians(kat))) <= 0:
    print('Trójkąt o zadanych parametrach nie istnieje')
else:
    if kat < 90:
        print(f'Trójkąt jest ostrokątny, a jego pole wynosi {(0.5 * a * b * m.sin(m.radians(kat))):.2}')
    elif kat == 90:
        print(f'Trójkąt jest prostokątny, a jego pole wynosi {(0.5 * a * b * m.sin(m.radians(kat))):.2}')
    else:
        print(f'Trójkąt jest rozwartokątny, nie można policzyć jego pola tym wzorem')
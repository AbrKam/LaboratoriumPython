import math as m

print('\n4. Napisz program rozwiązywania równania kwadratowego ax^2 + bx + c = 0, gdzie a, b i c są współczynnikami podawanymi przez użytkownika.\n')

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
c = int(input('Podaj współczynnik c: '))

print(f'\nWprowadzone równanie kwadratowe: {a}x^2 + {b}x + {c} = 0\n')

delta = (b**2) - (4*a*c)

if delta > 0:
    pdel = m.sqrt(delta)
    print(f'Delta = {delta}\nPierwiastek z delty = {pdel}\nx1 = {(-b - pdel)/ (2*a)}\nx1 = {(-b + pdel)/ (2*a)}')
elif delta == 0:
    print(f'Delta = {delta}\nx0 = {-b/(2*a)}')
else:
    print(f'Delta = {delta}\nBrak rozwiązań równania kwadratowego w zbiorze liczb rzeczywistych')



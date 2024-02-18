import random as r
import math as m

a = int(input('Podaj dolną granicę przedziału: '))
b = int(input('Podaj górną granicę przedziału: '))

krotka = [] #nie było podane żeby nie używać listy więc zrobiłem to na liście bo chyba najprościej ;p

for i in range(10):
    losowa = r.randint(a, b)
    krotka.append(losowa)

krotka = tuple(krotka)

iloczyn = 1

for i in krotka:
    iloczyn *= i

print(f'Krotka: {krotka}\nŚrednia geometryczna: {m.pow(iloczyn,1/10):.2}')
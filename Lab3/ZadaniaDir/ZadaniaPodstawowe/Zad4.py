import random as r

a = r.randint(3,7) #wygenerowanie losowej ilości elementów zbioru
b = r.randint(3,7)

x = set() #utworzenie pustych zbiorów
y = set()

i = 0

while i < a: #dodanie 'a' losowych elementów z przedziału <0,10> do zbioru
    x.add(r.randint(0,10))
    i += 1

i = 0

while i < b:
    y.add(r.randint(0,10))
    i += 1
    
print(f'Zbiór X: {x} \nZbiór Y : {y}') #wyświetlenie zbiorów żeby zobaczyć czy wszystko ok

#a Wypisz na ekran informację czy zbiór X zawiera liczbę 5.

if 5 in x:
    print('a) Zbiór X zawiera liczbę 5\n')
else:
    print('a) Zbiór X nie zawiera liczby 5\n')
    
if 5 in y:
    print('a) Zbiór Y zawiera liczbę 5\n')
else:
    print('a) Zbiór Y nie zawiera liczby 5\n')
    
#b Wypisz na ekran informację czy zbiór X jest podzbiorem zbioru Y.

z = 0

for i in x: #lub x <= y
    if i in y:
        z += 1 #za każdy element ze zbioru x należący do zbioru y dodaj +1 do z
    else:
        continue

if z == len(x): #jeśli z jest równy długości zbioru to znaczy, że wszystkie jego elementy należą do zbioru drugiego
    print("b) Zbiór X jest podzbiorem zbioru Y\n")
else:
    print('b) Zbiór X nie jest podzbiorem zbioru Y\n')

#c Wypisz na ekran informację czy zbiór Y jest podzbiorem zbioru X.

z = 0

for i in y:
    if i in x:
        z += 1
    else:
        continue

if z == len(y):
    print("c) Zbiór Y jest podzbiorem zbioru X\n")
else:
    print('c) Zbiór Y nie jest podzbiorem zbioru X\n')

#d Wypisz na ekran informację czy zbiór X jest nadzbiorem zbioru Y

z = 0

for i in y:
    if i in x:
        z += 1
    else:
        continue

if z == len(y):
    print("d) Zbiór X jest nadzbiorem zbioru Y\n")
else:
    print('d) Zbiór X nie jest nadzbiorem zbioru Y\n')
    
#e Wypisz na ekran informację czy zbiór Y jest nadzbiorem zbioru X.

z = 0

for i in x:
    if i in y:
        z += 1
    else:
        continue

if z == len(x):
    print("e) Zbiór Y jest nadzbiorem zbioru X\n")
else:
    print('e) Zbiór Y nie jest nadzbiorem zbioru X\n')
    
#f Wypisz na ekran sumę zbiorów X oraz Y

print(f'f) Suma zbiorów: {x | y}\n')

#g Wypisz na ekran różnicę zbiorów X oraz Y

print(f'g) Różnica zbioru X oraz Y: {x - y}\n')

#h Wypisz na ekran różnicę zbiorów Y oraz X.

print(f'h) Różnica zbioru Y oraz X: {y - x}\n')

#i Wypisz na ekran iloczyn zbiorów X oraz Y.

print(f'i) Iloczyn zbioru X oraz Y: {x & y}\n')

#j Wypisz na ekran różnicę symetryczną zbiorów X oraz Y 

print(f'j) Różnica symetryczna zbioru X oraz Y: {x ^ y}\n')

#k Wypisz na ekran wartość najwyższego elementu w obu zbiorach.

print(f'k) Największy element zbioru X: {max(x)}\n   Największy element zbioru Y: {max(y)}\n')

#l Usuń ze zbioru X pierwszy element i dołącz go do zbioru Y.

lx = list(x) #zrobienie nowej zmiennej będącej zbiorem x przekonwertowanym na liste, żeby można było zaindexować pierwszy jego element
pEle = lx[0] #przypisanie pierwszego elementu zbioru(listy) do zmiennej
x.remove(pEle) #usunięcie pierwszego elementu zbioru x ze zbioru x
y.add(pEle) #dodanie pierwszego elementu zbioru x do zbioru y

print(f'l) Zbiór X po usunięciu pierwszego elementu: {x}\n   Zbiór Y po dodaniu pierwszego elementu ze zbioru X: {y}\n')

#m Przekopiuj wszystkie elementy zbioru X do zbioru Y

Cy = y.copy()
Cx = x.copy()

print(f'm) Przekopiowane: {Cx | Cy}\n') #jako przekopiowanie mam rozumieć dodanie wszystkich elementów zbioru X do zbioru Y czy zastąpienie elementów zbioru Y elementami zbioru X? Jeśli to drugie to trzeba napisać y = x.copy()

#n Wyczyść oba zbiory

x.clear()
y.clear()

print(f'n) Zbiory po czyszczeniu: \n   X = {x}\n   Y = {y}')
#zad2

gotowaLista = [1,2,3,5,6,23,12]

sum = 0

for i in gotowaLista:
    sum += i

gotowaLista.insert(0, sum)

print(gotowaLista)
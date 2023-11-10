print('5. Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia wbudowanych funkcji\n')

#x = int(input('Wprowadz x: '))
#y = int(input('Wprowadz y: '))
#z = int(input('Wprowadz z: '))

#nie wiem czy oczekiwanym rozwiazaniem na tym etapie bylo zrobienie tego ifami, jesli tak to wygladalo by to mniej wiecej tak:
#if x > y and x < z:
#    print(y,x,z)
#elif x < y and y < z:
#    print(x,y,z)
#elif z < x and x < y:
#    print(z,x,y)
#elif z < x and z > y:
#    print(y,z,x)
#itd
#
#najlepiej byloby to zrobic tak:

list = []
i = 0

while i < 3:
    a = int(input('Wprowadz liczbe: '))
    list.append(a)
    i += 1

for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
        else:
            pass
        
print(list)
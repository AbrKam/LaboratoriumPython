def wypeln(a, b, c):
    lista = []
    for i in range(b ,a*c + b, c):
        lista.append(i)

    return lista

print(wypeln(4,3,3))
print(wypeln(2,5,7))
print(wypeln(6,8,7))
print(wypeln(5,7,2))
print(wypeln(1,7,4))
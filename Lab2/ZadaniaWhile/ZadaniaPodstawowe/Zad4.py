a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))



if a < b:
    #liczymy od a do b
    while a < b:
        if a%2 != 0:
            a += 1
            pass
        else:
            print(a)
            a += 1
elif a == b:
    print("a i b są równe")
else:
    while b <= a:
        #sprawdzamy wartosc modulo 2 z b, jesli jest rozne od 0 to jest to liczba nieparzysta i pomijamy, jak nie to ok
        if b%2 != 0:
            b += 1
            pass
        else:
            print(b)
            b += 1
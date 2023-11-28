liczbaG = int(input("Podaj liczbe gwiazdek: "))

for i in range(liczbaG):
#linia printujaca gwiazdki w wierszu
    for j in range(i+1):
        print("*", end = '')
    print("")

for i in range(liczbaG):
    print("*"*(i+1))

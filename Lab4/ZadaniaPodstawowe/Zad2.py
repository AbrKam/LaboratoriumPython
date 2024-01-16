def main():

    a = int(input('Podaj jeden bok: '))
    b = int(input('Podaj drugi bok: '))
    h = int(input('Podaj wysokość: '))
    print(f'Pole: {round(trapez(a, b, h), 2)} [jednostek^2]')

def trapez(a,b,h):
    return ((a + b) * h) / 2

main()
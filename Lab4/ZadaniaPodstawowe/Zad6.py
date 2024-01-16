def main():

    a = float(input('Podaj pierwszy bok a: '))
    b = float(input('Podaj drugi bok b: '))
    c = float(input('Podaj trzeci bok c: '))

    poleTrojkata(a, b, c)

def poleTrojkata(a,b,c):

    if a =< 0 or b =< 0 or c =< 0:
        print('Błędne dane')
    else:
        p = (a * b * c)
        pole = (p * (p - a) * (p - b) * (p - c))**0.5
        print(f'Pole trójkąta wynosi {pole}')

main()
def main():

    import math

    def pole(r):
        if r.isnumeric():
            p = math.pi * float(r) ** 2
            print(f'Pole wynosi {round(p, 2)} [jednostek^2]')
        else:
            print('Wprowadzono błędne dane')
            
    r = input("Wprowadź promień: ")
    pole(r)

main()
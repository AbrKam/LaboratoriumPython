import numpy as np

def zrobTablice(shape = (3,3), a = 0, b = 1, rows = 0, cols = 0):
    tablica = np.array(np.full(shape, a), ndmin = 2)
    print(tablica, '\n')
    
    for i in range(shape[0]):
        tablica[i, cols] = b # wspolrzedne podaje sie tablica[wiersz, kolumna], zeby zmienic sama kolumne o indexie np 0 trzeba dac wspolzedne kolumny jako stala i przeiterowac po wierszach, wtedy w kazdym wierszu zostanie zmieniona wartosc w odpowiedniej kolumnie
        tablica[rows, i] = b
    else:
        print(tablica, '\n')
        
    zero, jeden = 0, 0 

    for i in np.nditer(tablica):
        if i == 0:
            zero +=  1
        else:
            jeden += 1
    else:
        return f'ilość zer: {zero}', f'ilość jedynek: {jeden}'
    
print(zrobTablice())
print(zrobTablice((4,4),1,2,1,1))
print(zrobTablice((4,4),1,2,1,2))
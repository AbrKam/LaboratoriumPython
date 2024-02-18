import time as t

czas = int(input('Podaj czas [s]: '))

for i in range(0, czas):
    print(f'Czas do końca programu: {czas - i} [s]') 
    t.sleep(1)
else:
    print('Koniec ;D')

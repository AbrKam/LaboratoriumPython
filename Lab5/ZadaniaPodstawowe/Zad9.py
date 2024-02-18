import random as r

a = input('Podaj dolny zakres: ')
b = input('Podaj górny zakres: ')

while True:
    if  a.isalpha() or b.isalpha() or int(b) - int(a) <= 2: #jeżeli b - a = 2 to znaczy że w zgadywanym przedziale znajdują się trzy liczby przez co w 3 próbach gracz będzie w stanie na 100% zgadnąć wylosowaną liczbę
        print('Błędne dane, spróbuj jeszcze raz')
        a = input('Podaj dolny zakres: ')
        b = input('Podaj górny zakres: ')
    else:
        break

losowa = r.randint(int(a),int(b))

i = 0
j = 2 #dwa bo pierwsza informacja o ilości prób zostaje podana po wykorzystaniu pierwszej

while i < 3:
    zgaduj = int(input('Zgaduj: '))
    
    if zgaduj < losowa:
        print(f'Za mało, pozostałych prób {j}')
        i += 1
        j -= 1
    elif zgaduj > losowa:
        print(f'Za dużo, pozostałych prób {j}')
        i += 1
        j -= 1
    else:
        print(f'Zgadłeś! Wylosowana liczba to {losowa}')
        break


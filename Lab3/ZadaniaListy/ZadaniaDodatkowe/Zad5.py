zdanie = input('Wprowadź zdanie: ')

zdanie = zdanie.split() #podzielenie zdania wprowadzonego przez użytkownika na listę ze słowami
dlugosc = [] #pusta lista na potem

for i in zdanie: #zrobienie dodatkowej listy z długościami słów
    dlugosc.append(len(i))

razem = {k:v for (k, v) in zip(len(zdanie), zdanie)} #zip tworzy pare krotek z odpowiednich elementów z wprowadzonych list, specyfikujemy, że k odpowiada kluczom, v odpowiada wartościom
                                                 #dla każdej pary krotek utworzonych poprzez funckje zip dodajemy je do dictionary, gdzie tak jak sprecyzowano pierwsza wartość krotki to klucz, a druga to wartość

print(f'Najdłuższe słowo to "{razem[max(razem.keys())]}" ma ono długość {max(razem.keys())} znaków') #max(razem.keys()) zwraca największą wartość ze wszystkich kluczy, czyli w naszym przypadku najwięszką długość
                                                                                                     #dla tej długości wyciągamy odpowiadającą jej wartość z dicta razem[max(razem.keys())] - czyli nasze słowo
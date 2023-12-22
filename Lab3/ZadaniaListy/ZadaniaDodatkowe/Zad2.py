#2. Napisz program, który wczyta od użytkownika zdanie. Usuń z niego wszystkie znaki o 
#   nieparzystych indeksach. To co pozostało wypisz na ekran.

z = input("Wprowadź zdanie: ")

nowe = [] #pusta lista na nowe zdanie które będzie składać się ze znaków o parzystych numerach indexu

for index, znak in enumerate(z): #enumerate zwraca parę index, element z listy, w for loopie do każdej iteracji przypisujemy index do zmiennej index, a element do zmiennej znak
    if index%2 == 0: #jeżeli index daje resztę z dzielenia przez 2 równą 0 - jest parzysty, to dodajemy go do listy, która będzie tworzyć nowe zdanie
        nowe.append(znak)
    
print(f"Zdanie bez znaków o nieparzystych indexach: {''.join(nowe)}") #łączymy elementy listy za pomocą .join() żeby to w miarę ok wyglądało
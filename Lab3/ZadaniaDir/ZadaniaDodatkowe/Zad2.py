monety = [(1,1), (2,0), (3,3), (5,3)] #listy ze współrzędnymi monet oraz przeciwników
przeciwnicy = [(0,1), (2,3), (2,4), (3,4)] 

for y in range(4, -1, -1): #wysokość pola (y), iterujemy od 4 do 0 (-1 nie włącznie), co -1, czyli tak jakby od tyłu bo jak dałem range(5) to mi do góry nogami rysowało, więc tak sprecyzowany zakres mówiąc w skrócie 'odwraca rysownie'
    for x in range(6): #szerokość pola (x)
        if (x, y) in monety: #jeżeli odpowiednie współrzędne znajdują się w liście monety narysuj odpowiedni symbol 
            print(' * ', end = '')
        elif (x, y) in przeciwnicy: #jeżeli odpowiednie współrzędne znajdują się w liście przeciwnicy narysuj odpowiedni symbol
            print(' x ', end = '')
        elif y == 2: #jeśli współrzędna y wynosi 2 narysuj odpowiedni symbol
            print(' = ', end = '')
        else: #dla każdej innej kombinacji rysuj trawke
            print(' . ',end = '')
    print() #print zeby zaczynac rysowanie od nowej linii (\n) co każdą iteracje y
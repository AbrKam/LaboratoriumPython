#3. Napisz program, który wczyta od użytkownika zdanie. Wypisz je na ekran w taki 
#   sposób, że każdy jego wyraz będzie rozpoczynał się i kończył wielką literą.

zdanie = input("Wprowadź zdanie: ")

Zdanie = zdanie.title() #.title() robi, że każdy wyraz po spacji zaczyna się na dużą literę

pWyrazy = Zdanie.split(" ") #podzielenie zdania na wyrazy, podzielone wyrazy są przypisywane jako elementy nowej listy pWyrazy
nowe = []

#średnio mi się podoba to rozwiązanie ale działa
for i in pWyrazy:
    i = list(i)
    ostatnia = i[-1] #przypisanie ostatnie
    ostatnia = ostatnia.upper() #zmiana ostatniej litery na dużą
    i.pop() #usunięcie z danego wyrazu osatniej małej litery
    i.append(ostatnia) #dodanie na sam koniec listy dużej litery
    i = "".join([str(elem) for elem in i]) #połączenie ze sobą poszczególnych liter słowa iterując przez poszczególne litery; przed pętlą sprecyzowanie jakiego typu ma być interowana zmienna elem
    nowe.append(i) #dodanie zamienionego zdania do nowej pustej listy

print(f'Po zmianie: {" ".join(nowe)}') #połączenie słów z listy w jednego string'a





#--------------------------------------------------------------


#zdanie = input("Wprowadź zdanie: ")
#
#Zdanie = zdanie.title() #.title() robi, że każdy wyraz po spacji zaczyna się na dużą literę
#
#pWyrazy = Zdanie.split(" ") #podzielenie zdania na wyrazy, podzielone wyrazy są przypisywane jako elementy nowej listy pWyrazy
#
#zdanie = [elem[:-1] + elem[-1].upper() for elem in pWyrazy] #stworzenie nowej listy zdanie na podstawie listy pWyrazy zwierającej podzielone słowa, każdy element listy zdanie będzie składał się z połączenia elementu z listy pWyrazy
#                                                            #elem[:-1] wypisze wyraz bez ostaniej litery, natomiast elem[-1].upper() zmieni ostatnią literę z elementu na dużą literę, następnie te dwa stringi zostaną połączone za pomocą konkantenacji
#
#zdanie = ' '.join(zdanie)
#
#print(f'Zdanie : {zdanie}')
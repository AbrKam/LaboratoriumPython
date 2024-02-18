lista = ['dsada', 'dczcssx', 'daszzz', 'dasdzsxc', 'asa', 'a', 'sasaderixxx']

slownik = {i:len(lista[i]) for i in range(len(lista))} #utworzenie słownika z parami index(i) : długość stringa odpowiadającemu danemu indeksowi(len(lista[i]))

#puste słowniki do segragacji żeby pozniej je zapełnić 
nowySlownik = {}
slownikDoSegregowania = {}

for i in range(len(slownik)): #dla każdego i w range(len(slownik)), czyli poprostu dla każdej pary klucz:wartosc w slowniku
    nowySlownik.update({max(slownik): slownik[max(slownik)]}) #dodaj do nowySlownik maksymalna wartosc z kluczy (max(slownik)) w parze z odpowiadającej temu kluczowi wartością
    print(f'{max(slownik)}, {slownik[max(slownik)]}') #wypisanie słownika od największego klucza do najmniejszego
    del slownik[max(slownik)] #usuniecie dodanej wartosci ze slownika z ktorego pobieramy zeby nie byla ona juz brana pod uwage podczas korzystania z funckji max

nowaLista = [] #pusta lista na potem

doSegregacji = {len(lista[i]): lista[i] for i in range(len(lista))} # stworzenie nowej listy z parami dlugosc wyrazu i : wyraz i, dla wszystkich wyrazow z listy 'lista' 

for i in range(len(doSegregacji)): #iterowanie po kazdej parze klucz wartosc ze slownika doSegregacji
    nowaLista.append(doSegregacji[max(doSegregacji)]) # dodanie do utworzonej wczesniej pustej listy wartosci odpowiadajacej maksymalnej dlugosci ze wszsytkich dlugosci (kluczy) z doSegregacji 
    del doSegregacji[max(doSegregacji)] #tak jak wczesniej usuniecie maksymalnej wartosci ze slownika z ktorego pobieramy bo inaczej to dostalibysmy tylko liste z duplikatami tego stringa

print(nowaLista)
def main():
    
    print(anagram('kot','kokos'))
    print(anagram('niedziela','dzielnia'))
    print(anagram('Quid est veritas','Vir est qui adest'))
    
    
def anagram(a, b):
    wspolne = []
    
    a = a.lower().replace(' ', '') #zwiekszenie funkcjonalnosci, zeby wielkosc liter i ilosc spacji nie miala wplywu na wynik koncowy
    b = b.lower().replace(' ', '')
    
    for i in b:
        if i in a:
            wspolne.append(i) # zbieramy wszystkie wspolne znaki ze slowa 'b' wystepujace w slowie 'a' nawet z powtorzeniami
        else:
            continue
    if len(wspolne) == len(b): #jeli dlugosc wspolnych liter ze slowa a jest taka sama jak dlugosc slowa b to znaczy ze sa one anagramami
        return 'Słowa są anagramami'
    else:
        return 'Słowa nie są anagramami'
        
main()
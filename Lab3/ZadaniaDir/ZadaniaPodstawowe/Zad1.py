import random as r

n = int(input("Wprowadź liczbę elementów w liście: "))
x = int(input("Z ilu maksymalnie znaków mogą składać się ciągi: "))

#znaki ASCII A-Z od 65 do 90,      disclaimer: edit1: (tutaj pomiędzy są jeszcze chyba znaki typu // więc zrobiłem zadanie dla samych małych liter, żeby nie kompliować sobie zadania)
#            a-z od 97 do 122                  edit2: tak nie zauważyłem na początku, że Z = 90, kolejna literka a = 97, czyli na pewno coś musi być pomiędzy 

lSlowo = [] #pusta lista na znaki słowa
lElementow = [] #pusta lista na elementy

#generowanie losowych ciagów znaków
i = 0

while i < n:

    j = 0

    while j < r.randint(1,x): #losowa długość ciągu od 1 znaku do x zadane przez użytkownika
        lSlowo.append(chr(r.randint(97,122))) #przypisz do listy lSlowo losowy znak ASCII z przedziału od 65 do 122
        j += 1
    else:
        sSlowo = ''.join(lSlowo) #po wygenerowaniu słowa zmień je z listy na string
        lElementow.append(sSlowo) #przypisz przekonwertowane slowo do listy elementów
        lSlowo.clear() #czyscimy liste zeby kazde kolejne slowo nie zawieralo przedrostka z poprzedniego
        
    i += 1

print(f"\nWygenerowana lista: {lElementow}")

#a) Napisz program, który sprawdzi i wypisze na ekran ilość znaków w liście

razem = ''.join(lElementow) #połączenie ze sobą wszystkich elementów
lZnakow = len(razem) #policzenie ich
print(f"a) Liczba znaków w liscie wynosi: {lZnakow}")

#b) Napisz program, który sprawdzi i wypisze na ekran ile liter ‘k’ zawiera

k = 0

for i in razem:
    if i == 'k':
        k += 1
    else:
        continue

print(f'b) Liczba wystąpień litery "k" w liście: {k}')

#c) Napisz program, który sprawdzi i wypisze na ekran ile ciągów znaków: ‘kt’ zawiera

k = 0

for i in range(len(razem)): #range(len(razem)) żeby mieć inty bo przy napisaniu samego razem i byłby kolejnymi znakami w sekwencji i wyskakiwałby błąd, że chcemy dodać int do str
    if razem[i:i+2] == 'kt': #sprawdź od i do i + 2 (i + 2 bo przy specyfikacji od do bierze z od bez do; np. dla i = 0, razem[0:2] wypisze razem[0]razem[1])
        k += 1
    else:
        continue

print(f'Liczba ciągów znaków "kt" w wygenerowanych ciągach wynosi: {k}')

#d) Napisz program, który sprawdzi i wypisze na ekran ile ciągów znaków dłuższych niż s zawiera. Wartość s podaje użytkownik

s = int(input("c) Ciąg ma być dłuższy niż? (ile znaków): "))

m = 0

for i in lElementow:
    if len(i) > s:
        m += 1
    else:
        continue
    
print(f"d) Liczba ciągów posiadająca więcej znaków niż {s}: {m}")

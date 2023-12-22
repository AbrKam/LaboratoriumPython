#1. Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery 
#   w kolejności alfabetycznej, a następnie wypisze których litera alfabetu nie zawiera.

z = input("Wprowadź zdanie: ")

z.lower #.lower żeby wielkość znaku wprowadzana przez użytkownika nie miała znaczenia

z = list(z) #zmiana typu str na liste aby można było użyć funkcji pythona .sort
z.sort() #posortowanie alfabetycznie elementów listy

print(f"Alfabetycznie: {', '.join(z)}") # "".join pozwala na wyświetlenie listy 'w inny sposób'; zamiast ['a', 'b', ...] można pozbyć się nawiasu kwadratowego i ustalić separator między elementami

alfabet = 'aąbcćdeęfghijklmnoóprstuwxyz'
alfabet = list(alfabet) #zmiana typu ze str na list żeby można było użyć .remove()

for i in alfabet: #przejdź przez każdy element w alfabet
    if i in z: #jeśli ten element znajduje się we wprowadzonym przez użytkownika słowie
        alfabet.remove(i) #usuń go z alfabetu
    else: #jeśli element nie znajduje się we wprowadzonym słowie nic nie rób
        pass
    
print(f"Litery których zdanie nie zawiera to: {alfabet}") #tutaj zostawiłem normalne printowanie listy bo wydaje mi się, że w tym przypadku jest czytelniej
print( '\n1. Stwórz automatyczny cennik biletowy: \n• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.\n• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.\n• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.\n')

wiek = int(input('Wprowadź wiek klienta: '))

if wiek > 18:
    print('Cena biletu: 20 zł')
elif wiek >= 4:
    print('Cena biletu: 10 zł')
elif wiek < 0:
    print('Wprowadzono zły wiek! >:(')
else:
    print('Cena biletu: free')

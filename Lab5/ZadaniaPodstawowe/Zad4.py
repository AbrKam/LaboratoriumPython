import datetime as dt

dataKolokwium = dt.datetime(2024,2,11,16,20,00)
dataOstLab = dt.datetime(2024,2,10,8,00,00)
teraz = dt.datetime.now()
kiedyKolos = dataKolokwium - dataOstLab

print(f'Ostatnie zajęcia odbyły się {dataOstLab:%B %d, %Y}, a kolokwium odbędzie się {kiedyKolos} po nich tj. {dataKolokwium:%B %d, %Y}')

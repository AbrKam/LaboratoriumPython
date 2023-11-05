import random

#4
# droga = int(input("Podaj drogę przebytą przez samochód [km]: "))
#4.1
droga = random.randint(1,100000)
spalanie = int(input("Podaj średnie spalanie [l/100km]: "))

cena = 6.5 #[zl/l]

zuzycie = droga * spalanie / 100

koszt = zuzycie * cena

print(f"Przy przejechaniu {droga} km ze spalaniem rzędu {spalanie} l/100km zużyjesz {zuzycie} litrów paliwa, co będzie Cie kosztować {koszt} zł")

imie = input("Wprowadź imie: ")
print("Witaj, ", imie)

wiek = input("Wprowadź swój wiek: ")
print("Twój wiek to: ", wiek)

imie = input("Wprowadź imie: ")
nazwisko = input("Wprowadź nazwisko: ")
print("Twoje inicjały: ", imie[0], nazwisko[0])

lancuch = input("Podaj łańuch: ")
print("łańuch razy 5: ", 5 * lancuch)

lancuch1 = input("Wprowadź łancuch 1: ")
lancuch2 = input("Wprowadź łańcuch 2: ")
lancuch3 = lancuch1 + lancuch2
print("Połączenie łańcuchów: ", lancuch3)

lancuch1 = input("Wprowadź łancuch 1: ")
lancuch2 = input("Wprowadź łańcuch 2: ")
lancuch3 = lancuch1[0:int(len(lancuch1)/2)] + lancuch2[int(len(lancuch2)/2):]
print("Połączenie łańcuchów pol pol: ", lancuch3)

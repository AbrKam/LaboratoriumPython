rachunki = {"wrzesień": 50, "październik": 65, "listopad": 57, "grudzień": 72}

print(f"Suma rachunków: {sum(rachunki.values())}")
print(f"Max rachunek: {max(rachunki.values())}")
print(f"Min rachunek: {min(rachunki.values())}")
print(f"Średnia rachunków: {sum(rachunki.values())/len(rachunki)}")

#jak wyciagnac ostatni ze slownika
klucze = list(rachunki.keys())
print(klucze[-1])

ostatni = klucze[-1]
srednia = sum(rachunki.values()) / len(rachunki)

if ostatni > srednia:
    print("Zacznij oszczedzac")
else:
    print("Jest ok")
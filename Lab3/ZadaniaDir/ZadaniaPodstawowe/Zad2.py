listaZakupow = {"Czekolada": 8, "Mleko": 2, "Nie mleko": 3}
print(listaZakupow)

suma = sum(listaZakupow.values())
print(f"Suma wydatków z zakupów (sum): {suma} [zł]")

ceny = list(listaZakupow.values())
suma = 0

for i in ceny:
    suma += i
else:
    print(f"Suma wydatków z zakupów (for): {suma} [zł]")
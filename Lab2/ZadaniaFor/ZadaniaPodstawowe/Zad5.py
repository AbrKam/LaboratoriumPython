n = int(input("Wprowadź liczbę naturalną n dla której chcesz obliczyć silnię: "))

silnia = 1

for i in range(n):
    silnia *= (i + 1)
else:
    print(f"Silnia liczby {n} wynosi: {silnia}")
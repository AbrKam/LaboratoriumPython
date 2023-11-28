n = int(input("Podaj ilość studentów w grupie: "))

i = 1

sum = 0

while i <= n:
    x = int(input(f"Wprowadź liczbę punktów dla {i} studenta: "))
    sum += x
    i += 1
else:
    print(f"Średni wynik w grupie wyniósł: {sum/n:.2f} pkt.")
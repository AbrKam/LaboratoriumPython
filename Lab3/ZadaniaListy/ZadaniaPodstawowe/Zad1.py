
n = 0
imiona = []

while n < 4:
    imie = input("Wprowadź imię: ")
    imiona.append(imie)
    n += 1

print("Posortowane: ", sorted(imiona))

j = 0

while j < 2:
    imie = input("Wprowadź kolejne imiona: ")
    imiona.insert(len(imiona),imie)
    j += 1

print("Ostatnia osoba: ", imiona.pop())
print("Lista imion bez imiona wyżej: ", imiona)

imie = input("Dodaj jeszcze jedną osobę: ")

imiona.insert(2, imie)
imiona.reverse()

print("Odwrócone: ", imiona, "\nZdublowane odwrócenie: ", 2*imiona)

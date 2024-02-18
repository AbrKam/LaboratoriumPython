#zad4

a = str(input('Podaj ciąg znaków: '))

j = 0

for i in a:
    if i != a or i != b:
        j += 1

print(f'Znaków różnych od "a" i "b" jest {j}')
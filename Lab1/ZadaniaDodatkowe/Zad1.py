print('\n1. Napisz program wyznaczania wartości funkcji określonych wzorami dla argumentów rzeczywistych podawanych przez użytkownika\n\n          [ 2*x dla x > 0\na) a(x) = { 0 dla x = 0\n          [ -3*x dla x < 0\n\n          [ x^2 dla x >= 1\nb) b(x) = { \n          [ x dla x < 1\n\n          [ 2 + x dla x > 2\nc) c(x) = { 8 dla x = 2\n          [ x - 4 dla x < 2\n')

x = int(input('Podaj wartość x: '))

#a(x)

if x > 0:
    print(f"Wartość funkcji a(x) = {2 * x}")
elif x == 0:
    print(f"Wartość funkcji a(x) = {0 * x}")
else:
    print(f"Wartość funkcji a(x) = {-3 * x}")

#b(x)

if x >= 1:
    print(f"Wartość funkcji b(x) = {x ** 2}")
else:
    print(f"Wartość funkcji b(x) = {x}")

#c(x)

if x > 2:
    print(f"Wartość funkcji c(x) = {2 + x}")
elif x == 2:
    print(f"Wartość funkcji c(x) = {8}")
else:
    print(f"Wartość funkcji c(x) = {x - 4}")

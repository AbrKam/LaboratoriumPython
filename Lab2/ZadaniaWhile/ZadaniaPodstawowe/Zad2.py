print("Program wyświetla wartość funkcji y = 2x^2 - 5x - 8, dla x z przedziału od -4 do 4\n")

x = -4

#dopóki wartość x jest mniejsza lub równa 4 wykonuj pętle
while x <= 4:
    #wypisz wartość funkcji dla bieżącego x
    print(f"Wartość funkcji wynosi {2*x**2 - 5*x - 8:.1f} dla x = {x:.1f}\n")
    #zwiększ x o podany w zadaniu krok
    x += 0.5
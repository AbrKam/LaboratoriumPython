
#Nie wiem czy dobrze zrozumiałem zamysł tego zadania. Czy jest możliwość zobaczenia przykładowego rozwiązania?
#bez zastosowania funkcji try: i except ValueError: nie mam pomysłu jak inaczej to napisać, szczególnie na dwa sposoby z continue i bez
#i czy ten program miał być napisany na pętli for zamiast while? Ponieważ jest pod zadaniami z części for, a z wykorzystniem tej pętli nie 
#mam pomysłu jak to wykonać

while True:
    x = input("Wprowadź zmienną: ")

    if x.isnumeric() == True and int(x) > 0:
        print("To jest liczba")
        print(f"Pierwiastek kwadratowy liczby: {int(x)**0.5:.2f}")
        continue
    else:
        print('Dziękujemy za skorzystanie z naszej aplikacji')
        break

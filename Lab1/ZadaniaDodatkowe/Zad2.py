print('2. Z wykorzystaniem operatorów logicznych not (negacja) oraz and (koniunkcja) napisz \nprogram, który w zależności od spełnienia pewnych warunków wyświetla \nodpowiednie komunikaty:\n\n• Jeśli pada deszcz i jest autobus na przystanku, to „Weź parasol”, „Dostaniesz się na uczelnie”; \n• Jeśli pada deszcz i nie ma autobusu, to „Nie dostaniesz się na uczelnię”; \n• Jeśli nie pada deszcz i jest autobus na przystanku, to „Dostaniesz się na uczelnie”, „Miłego dnia i pięknej pogody”. \n')

a = input("Czy pada deszcz? (Tak/Nie) ")
d = input("Czy jest autobus? (Tak/Nie) ")

if a == 'Tak':
    a = True
else:
    a = False

if d == 'Tak':
    d = True
else:
    d = False

if a and d:
    print('Weź parasol”, „Dostaniesz się na uczelnie')
elif not a and d:
    print("Dostaniesz się na uczelnie, Miłego dnia i pięknej pogody")
else:
    print('Nie dostaniesz się na uczelnię')

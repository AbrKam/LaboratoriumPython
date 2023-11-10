print('\n2. Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała\n')

a = input('Wprowadź literę: ')

if a.isupper() == True:
    print('Wprowadzona litera jest duża')
else:
    print('Wprowadzona litera jest mała')
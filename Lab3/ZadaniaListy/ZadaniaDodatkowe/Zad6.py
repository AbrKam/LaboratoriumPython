z = input('Wprowadź ciąg znaków: ')

y = list(z) #zmiana ciągu znaków na listę żeby można było użyć .reverse()

y.reverse() #odwrócenie kolejoności znaków

y = ''.join(y) #złożenie listy z powrotem do stringa

if y == z: #jeżeli y == z to znaczy, że są takie same -> słowo po odwróceniu jest takie samo jak słowo przed odwróceniem = jest palindromem
    print('To słowo jest palindromem')
else:
    print('To słowo nie jest palindromem')

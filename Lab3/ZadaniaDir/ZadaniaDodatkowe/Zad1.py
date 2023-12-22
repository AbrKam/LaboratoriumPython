liczby = input('Wprowadź 5 liczb rozdzielonych przecinkiem: ')

liczby = liczby.replace(' ', '').split(',') #.replace(' ', '') żeby usunąć spacje, jeśli użytkownik chciałby ją dać po przecinku, podzielenie wprowadzonego przez użytkownika stringa .split(',') na listę liczb,
                                            #funkcja dzieli co ','

if len(liczby) != 5: #jeśli długość listy nie wynosi 5 poinformuj użytkownika o wprowadzeniu nieodpowiedniej liczby elementów
    print('Nie wprowadzono 5 liczb!')
else:
    losowosc = set(liczby) #zrobienie z wprowadzonych przez użytkownika liczb zbioru

    los = losowosc.pop() # 'wylosowanie' elementu ze zbioru z wykorzystaniem funkcji .pop()

    if los == max(liczby): #jeśli wylosowano max z podanych liczb poinformuj odpowiednim komunikatem
        print(f'Wow! Wylosowano {los} jest ona największa z podanych liczb!')
    elif los == min(liczby): #jeśli wylosowano min z podanych liczb poinformuj odpowiednim komunikatem
        print(f'Wow! Wylosowano {los} jest ona najmniejsza z podanych liczb!')
    else:
        print(f'Wylosowano {los}!')
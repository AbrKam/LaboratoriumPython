n = int(input('Podaj wartość n: '))

alfabet = list('abcdefghijklmnoprstuqxyz')

nowe = [alfabet[i: i + n] for i in range(0, len(alfabet), n)] #stwórz listę gdzie każdy kolejny element dodawany podczas iteracji bedzie zawierał od i do i+n elementów, gdzie na samym początku i = 0
                                                              #iteruj przez całą listę (od 0 do len(alfabet)) co n-ty element
print(nowe)
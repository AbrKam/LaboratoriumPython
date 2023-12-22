#4. Napisz program, który zamieni w ciągu znaków podanym przez użytkownika każdy 
#   znak, który się powtórzy na @. Zmieniony ciąg znaków wypisze na ekran.

a = input('Wprowadź ciąg znaków: ')

coJuzBylo = [] #pusta lista do storowania literek które już były 
nowe = [] #pusta lista do stworzenia nowego zdania z podmienionymi literami które się powtarzają

for i in a: #dla każdej literki we wprowadzonym słowie
    if i in coJuzBylo: #jeżeli dana literka już była
        nowe.append('@') #to wstaw w jej miejsce @
    else:
        coJuzBylo.append(i) #jeśli jej nie było dodaj ją do listy, żeby przy następnym powtórzeniu pętli program wiedzał, że już była
        nowe.append(i) #przepisz tą samą literkę bez zmiany w jej miejsce 

print(''.join(nowe)) #połączenie powstałej listy z nowym słowem w stringa
        
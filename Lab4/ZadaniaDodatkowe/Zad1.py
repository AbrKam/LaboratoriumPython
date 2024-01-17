def main():
    
    imiona = ['Agnieszka', 'Damian', 'Michał', 'Sebastian', 'Daniel']
    dict = {imie: plec(imie) for imie in imiona}
    print(dict)
    
def plec(s):
    if s[-1] == 'a':
        return 'kobieta'
    else:
        return 'mężczyzna'
    
main()
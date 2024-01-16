def main():

    imie = input('Jak masz na imie? ')
    wiek = input('Ile masz lat? ')

    imiewiek(imie, wiek)

    imiewiek('Tadek', 23)
    imiewiek('Jarek')

    print(imiewiek.__doc__)

def imiewiek(imie, wiek = 20):
    """ komentarz """
    print(f'twoje imie to {imie} i masz {wiek} lat')

main()
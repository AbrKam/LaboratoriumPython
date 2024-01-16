def main():

    waga = float(input('Podaj swoją wagę [kg]: '))
    wzrost = float(input('Podaj swóją wzrost [m]: '))

    BMI(waga, wzrost)

def BMI(waga, wzrost):

    if wzrost < 0 or waga < 0:
        print('Wprowadzono błędne dane')
    else:
        bmi = round(waga / (wzrost ** 2), 2)

        if 18.49 >= bmi >= 17:
            print(f'Twoje BMI wynosi {bmi} i masz niedowagę')
        elif 24.99 >= bmi >= 18.50:
            print(f'Twoje BMI wynosi {bmi} i masz prawidłową wage')
        elif 30.00 >= bmi >= 25.00:
            print(f'Twoje BMI wynosi {bmi} i masz nadwagę')
        elif 34.99 >= bmi >= 30.00:
            print(f'Twoje BMI wynosi {bmi} i masz otyłość')
        else:
            print('Wynik poza zakresami')

main()
def main():

    print('3. Napisz program (funkcję), który zamieni małą literę na dużą lub odwrotnie – dużą na małą.')

    a = input('Wprowadź literę: ')

    conv(a)

def conv(x):
    if x.isupper() == True:
        return print(x.lower())
    else:
        return print(x.upper())
    
main()
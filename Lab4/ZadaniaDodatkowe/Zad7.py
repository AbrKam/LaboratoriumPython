def main():
    
    palindrom('kot')
    palindrom('kajak')
    
def palindrom(z):
    y = list(z) 
    y.reverse()

    y = ''.join(y)

    if y == z:
        print(f'To słowo ({z}) jest palindromem')
    else:
        print(f'To słowo ({z}) nie jest palindromem')

main()
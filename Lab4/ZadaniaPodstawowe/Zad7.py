def main():
    
    odwrot()

def odwrot():
    a = list(input('Podaj string: '))
    a.reverse()
    print(f'Odwrócone: {"".join(a)}')
    
main()
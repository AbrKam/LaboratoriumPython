def main():
    
    print(kwadratowa(1,1,1))
    print(kwadratowa(1))
    print(kwadratowa(2))
    print(kwadratowa(2,-1,-4))
    print(kwadratowa(2,4,1))
    print(kwadratowa(2,4))
    print(kwadratowa(2,-1,4))
        
def kwadratowa(a, b = 0, c = 0):
    
    delta = (b ** 2) - (4 * a * c)
    pDel = (delta)**0.5
    
    if delta > 0:
        x1 = (-b - pDel) / (2*a)
        x2 = (-b + pDel) / (2*a)
        return (x1,x2)
    elif delta == 0:
        x0 = -b/(2*a)
        return (x0,)
    else:
        return 'Delta mniejsza od 0, brak miejsc zerowych w R'
            
main()
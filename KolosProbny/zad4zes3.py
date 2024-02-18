def elementy(tablica, a, b):
    nowe = tablica[a:b]
    
    sum = 0
    
    for i in nowe:
        sum += i
    else:
        sred = sum/len(nowe)
        
    return sred

tab = [1, 2, 3, 4, 5, 6, 7, 8]

print(elementy(tab, 2, 4))
print(elementy(tab, 0, len(tab)))
print(elementy(tab, 0, 3))
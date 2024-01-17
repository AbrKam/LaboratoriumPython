def main():
    
    print(liczLitery('AbCdE'))
    print(liczLitery('@bCdE$'))
    print(liczLitery('Abcde'))
    print(liczLitery('AAAAA'))
    print(liczLitery('$$$$'))
    
def liczLitery(s):
    duze = 0
    male = 0
    reszta = 0
    for i in s:
        if i.isupper():
            duze +=1
        elif i.islower():
            male += 1
        else:
            reszta +=1
    
    znaki = {'duże':duze,'małe':male,'reszta':reszta}
    return znaki

main()
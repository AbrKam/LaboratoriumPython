print('\n1. Napisz program rozwiązywania równania liniowego 0 = ax + b, gdzie a i b są współczynnikami podawanymi przez użytkownika\n')

a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))

# 0 = ax + b / -b
#-b = ax / :a
#-b/a = x

if a == 0:
    print("a musi być różne od 0!")
else:
    x = -b/a
    print(f"Rozwiązaniem równania liniowego dla podanych współczynników jest x = {x}")
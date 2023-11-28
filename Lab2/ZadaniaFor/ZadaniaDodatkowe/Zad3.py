#dodatek do zadania 3 z wyśrodkowaniem choinki

liczbaG = int(input("Podaj liczbe gwiazdek: "))
#
#for i in range(liczbaG):
##linia printujaca gwiazdki w wierszu
#    for j in range(i+1):
#        print("*", end = '')
#    print("")

j = liczbaG

for i in range(liczbaG):
    print(" "*j, end = "")
    print("*"*(i+1))
    j -= 1

#  *
# **
# ***
#****
#*****

#?

#  *
#  **
#  ***
# ****

#  *
# ***
#*****
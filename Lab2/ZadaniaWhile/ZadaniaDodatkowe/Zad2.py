#----------Część 1 modyfikacji---------------------------------
   
#n = int(input("Podaj ilość studentów w grupie: "))
#
#i = 1
#
#sum = 0
#
#while i <= n:
#    
#    x = int(input(f"Wprowadź liczbę punktów dla {i} studenta: "))
#    
#    if x in range(0,101):
#        sum += x
#        i += 1
#    else:
#        continue
#else:
#    print(f"Średni wynik w grupie wyniósł: {sum/n:.2f} pkt.")

#--------------------------------------------------------------

#----------Część 2---------------------------------------------

i = 1

sum = 0

while True:
    x = int(input(f"Wprowadź liczbę punktów dla {i} studenta: "))
    if x in range(0,101):
        sum += x
        print(f"Średni wynik w grupie składającej się z {i} studentów wyniósł: {sum/i:.2f} pkt.")
        i += 1
    #nie wiem czy dobrze zrozumiałem intencję wyjscia z programu break'iem
    else:
        print("Podano liczbę spoza przedziału 0 - 100, koniec :(")
        break

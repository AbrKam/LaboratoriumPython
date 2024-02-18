import random as r

#a

print(f'Szczęśliwy numerek {r.randint(1,100)}')

#b

roczniki = []

for i in range((2004 - 1980) + 1): #nie gwarantuję, że założone roczniki pokrywają się ze stanem faktycznym, od 1980 do 2004 z 1980, dlatego + 1
    roczniki.append(i + 1980)
    
print(f'Roczniki: {roczniki}')
print(f'Szczęśliwy rocznik: {r.choice(roczniki)}')

#c

doLosowania = []

for i in range(0,49):
    doLosowania.append(i+1)
    
print(f"Totolotek: {r.sample(doLosowania, 6)}")
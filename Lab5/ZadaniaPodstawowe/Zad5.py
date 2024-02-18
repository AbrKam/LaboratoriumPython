import keyword as k

slowaKluczowe = ['for', 'print', 'break', 'done', 'bad']

takToSlowaKluczowe = []

for i in slowaKluczowe:
    if k.iskeyword(i):
        takToSlowaKluczowe.append(i)
    else:
        pass

print(f'Slowa klczowe: {takToSlowaKluczowe}')
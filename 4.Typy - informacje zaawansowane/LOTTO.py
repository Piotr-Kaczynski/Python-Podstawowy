import random
moje_numery = []
while len(moje_numery) < 7:
    numer = random.randint(1, 49)
    if numer in moje_numery:
        continue
    moje_numery.append(numer)
print(moje_numery)

########### LAB ############
print('\n########### LAB #############')

kolory = ['kier', 'karo', 'trefl', 'pik']
figury = ['As', 'Król', 'Dama', 'Walet', '10', '9']

karty = []

for figura in figury:
    for kolor in kolory:
        karta = figura
        karta += ' ' + kolor
        karty.append(karta)

random.shuffle(karty)
print(karty)

gracz1 = []
gracz2 = []

for i in range(len(karty)):
    if i%2==0:
        gracz1.append(karty[i])
    else:
        gracz2.append(karty[i])

print(gracz1)
print(gracz2)

gracz1 = karty[:12]
gracz2 = karty[12:]
print(gracz1)
print(gracz2)

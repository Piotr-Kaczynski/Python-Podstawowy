# aCard = {'Figura':'Król', 'Moc':12}
# print(aCard)
# print(aCard['Figura'])
# print(aCard['Moc'])
import random

kolory = ['Kier', 'Karo', 'Trefl', 'Pik']
figury = [
    {'Figura':'As',      'Moc':14},
    {'Figura':'Król',    'Moc':13},
    {'Figura':'Królowa', 'Moc':12},
    {'Figura':'Walet',   'Moc':11},
    {'Figura':'10',      'Moc':10},
    {'Figura':'9',       'Moc':9}]

wszystkieKarty = []
for kolor in kolory:
    for figura in figury:
        karta = figura.copy()
        karta['Kolor'] = kolor
        wszystkieKarty.append(karta)


random.shuffle(wszystkieKarty)
gracz1 = wszystkieKarty[:12]
gracz2 = wszystkieKarty[12:]

print('Karty gracza1:')
print(gracz1)
print('\nKarty gracza2:')
print(gracz2, '\n')

i = 0
while len(gracz1) > 0 and len(gracz2) > 0:
    karta1 = gracz1.pop(0)
    karta2 = gracz2.pop(0)
    print('1#    %3d    VS %3d    2#' %(karta1['Moc'], karta2['Moc']))
    if karta1['Moc'] > karta2['Moc']:
        gracz2.append(karta1)
        gracz2.append(karta2)
        print('       Wygrał gracz 1\n')
    elif karta1['Moc'] < karta2['Moc']:
        gracz1.append(karta2)
        gracz1.append(karta1)
        print('       Wygrał gracz 2\n')

    elif karta1['Moc'] == karta2['Moc']:
        print('            REMIS')
        gracz2.append(karta2)
        gracz1.append(karta1)
if len(gracz2) > 0:
    print('WYGRAŁ GRACZ 1')
else:
    print('WYGRAŁ GRACZ 2')

liderzy = {'PL':'Duda', 'US':'Trump'}
#{klucz : wartość}
print(liderzy)

print(liderzy['US']) #wywołanie wartości za pomocą klucza
liderzy['DE'] = 'Merkel' #dodanie elementu do słownika
print(liderzy)

print(liderzy.keys()) #zwraca same klucze
print(liderzy.values()) #zwraca same wartości
print(liderzy.items()) #zwraca elementy słownika(klucz i wartość)

print(liderzy.popitem())

print(liderzy.setdefault('FR', 'Macron')) #dodaje element

print(liderzy.get('RU')) #jeżeli nie ma wartości to zwraca None

newLiders = {'RU':'Putin', 'DE':'Schulz'}
print(newLiders)
liderzy.update(newLiders)


print(liderzy)


################## LAB ###################
print('\n################## LAB ###################')

#1
chanels = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV Spot':700}
print(chanels)

#2
print(chanels['Email'])

#3
chanelUpdates = {'Natural Traffic':520, 'News':600}
print(chanelUpdates)

#4
chanels.update(chanelUpdates)
print(chanels)

#5
print(chanels.keys())

#6
chanels.pop('Email')
print(chanels)
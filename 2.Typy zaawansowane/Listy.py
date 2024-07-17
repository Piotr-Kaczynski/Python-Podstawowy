lista = ['PL', 'US', 'RU', 'GB']
print(lista)
print(lista[1])

lista[1] = 'NL'
print(lista)
lista.append('DE')
print(lista)
lista.insert(4, 'FI')
print(lista)
lista.remove('RU')
print(lista)
lista.sort() #in place
print(lista)
print(lista.pop(3), lista) #usuwa element z listy
print(lista.index('PL'))
print(lista.count('PL'))

nowa = ['SK', 'IT']
lista.extend(nowa) #rozszerza liste o nową liste
print(lista)
# lista_kopia = lista   #zmiana jednej z list wpłynie na obydwie
# lista_kopia.clear()
# print(lista)
# print(lista_kopia)

lista_kopia = lista.copy()   #tworzy kopie listy nad którą można pracować
lista_kopia.clear()
print(lista)
print(lista_kopia)

############## LAB ##############
print('\n############## LAB ##############')
hity = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']

#2
hity.append('CHILD IN TIME')
hity.append('AGAIN')

#3
hity.insert(2, 'HOTEL CALIFORNIA')

#4
hity.insert(0, 'THE SOUND OF SILENCE')

#5
print(hity.index('HOTEL CALIFORNIA'))

#6
hity.remove('HOTEL CALIFORNIA')

#7
hity[0] = 'ENJOY THE SILENCE'

#8
hitsToRead = hity.copy()

#9
hitsToRead.reverse()

#10
hitsToRead.sort()

#11
print(hitsToRead[0])
hitsToRead.pop(0)
print(hitsToRead[0])
hitsToRead.pop(0)

#12
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']

#13
hitsToRead.extend(additionalSongs)

#14
print('Wish you were here:', hitsToRead.count('WISH YOU WERE HERE'), '  Riders on the storm:', hitsToRead.count('RIDERS ON THE STORM'))

#15
hitsToRead.clear()





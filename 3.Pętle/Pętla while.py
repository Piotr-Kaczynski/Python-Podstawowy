################# LAB #################
#Ładowanie paczek do kontenera
import random

#1
for i in range(50):
    print(str(i)+'+'+ str(i+1),'=',i+i+1)

#2
proba = 1
numer = random.randint(0, 20)
print('Zgadnij liczbę z przedziału <0,20>')
x = int(input('Podaj swoją liczbę:'))
while x != numer:
    if x > numer:
        print('Nie zgadłeś, liczba jest mniejsza')
    elif x < numer:
        print('Nie zgadłeś, liczba jest większa')

    x = int(input('Podaj swoją liczbę:'))
    proba +=1
else:
    print('Brawo, liczba to:', numer,' Zgadłeś za', proba, 'razem')



import datetime
import random

print(datetime.MINYEAR, datetime.MAXYEAR) #wartości minimane i maksymalne dla lat

#TIMEDELTA
roznica = datetime.timedelta(days=1, hours=2, minutes=-30) #wyznaczanie różnicy czasu
print(roznica)

roznica2 = datetime.timedelta(days=-3, hours=-5, minutes=-13) #wyznaczanie różnicy czasu wstecz
print(roznica2)

print('Suma różnic', roznica + roznica2)

#DATE
dzisiaj = datetime.date.today()
dniDoZaplaty = datetime.timedelta(days=7)
print('Dziś jest:', dzisiaj)
print('Musisz zapłacić do:', dniDoZaplaty)
print('Musisz zapłacić do:', dniDoZaplaty + dzisiaj)

koniec_swiata = datetime.date.max
print('Pajtonowski koniec świata:', koniec_swiata)
print('Pajtonowski koniec świata odbedzie sie dnia tygodnia numer:', koniec_swiata.weekday())

urodzenie = datetime.date(2005, 8, 17)
print('Ten ktoś ma', dzisiaj - urodzenie, 'dni')

#DATETIME
print('Teraz', datetime.datetime.now())
print('Dziś', datetime.datetime.today())
print('UTC teraz', datetime.datetime.utcnow())
print('Dzisiejszy dzień tygodnia', datetime.datetime.today().weekday())

print('%a', datetime.datetime.now().strftime('%a'))
print('%A', datetime.datetime.now().strftime('%A'))
print('%w', datetime.datetime.now().strftime('%w'))
print('%Y-%m-%d %H_%M_%S_%f', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S_%f')) # %F - milisekundy

############ LAB ##############
import math
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

#1
print('\nZadanie 1')
len_inputdata = len(inputdata)
len_factortable = len(factortable)

print(len_inputdata, len_factortable)

if len_inputdata == len_factortable:
    for i in range(len(inputdata)):
        minvalue = (inputdata[i] - factortable[i]) * inputdata[i]
        maxvalue = (inputdata[i] + factortable[i]) * inputdata[i]
        print(minvalue, maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, inputdata[i], maxinteger)

else:
    print('Te listy nie mjaą tyle samo elementów')

#2
print('\nZadanie 2')
for i in range(len(inputdata)):
    minvalue = (inputdata[i] - random.random()) * inputdata[i]
    maxvalue = (inputdata[i] + random.random()) * inputdata[i]

#3
print('\nZadanie 3')
from datetime import datetime

print(datetime.today())
print(datetime.today().strftime('%Y-%m-%d'))




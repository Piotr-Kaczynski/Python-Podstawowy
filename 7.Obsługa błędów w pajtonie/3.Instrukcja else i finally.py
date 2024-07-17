import sys
import os
# zadania_na_osobe = 0
# try:
#     zadania = 32
#     osoby_str = input('Ile jest osób w zespole: ')
#     osoby = int(osoby_str)
#     zadania_na_osobe = zadania / osoby
#
# except ValueError as e: #tworzenie zmiennej 'e' dla błędu którą następnie możemy wyświetlić
#     print('Musisz wpisać liczbę: ', e)
# except ZeroDivisionError as e:
#     print('Nie można wprowadzić zera ', e)
# else: #zostanie wyświetlone tylko wtedy kiedy program nie napotkał żadnego błędu
#     print(zadania_na_osobe)
#
# finally: #blok ten zostanie wykonany niezależnie od napotkanych błędów
#     print('Program zakończył się')

########### LAB ###########

#1
wejscie = input('Ile masz lat: ')
path = input('Podaj ścieżkę do pliku: ') #C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt

# plik = open(sciezka, 'w+')
# plik.write(wejscie)
# plik.close()

#2
# try:
#     plik = open(sciezka, 'w+')
#     plik.write(wejscie)
#     plik.close()
# except:
#     print('Napotkano błąd')

#3
try:
    plik = open(path, 'w')
    plik.write(wejscie)
    plik.close()
    wejscie_int = int(wejscie)
    print('Zapisano:', wejscie_int)

except FileNotFoundError:
    print('Błąd otwierania pliku', path, sys.exc_info()[0])
except ValueError:
    print('Podana wartość musi być liczbą', wejscie, sys.exc_info()[0])
except:
    print('Napotkano błąd')
else:
    print('Program zakończył się')
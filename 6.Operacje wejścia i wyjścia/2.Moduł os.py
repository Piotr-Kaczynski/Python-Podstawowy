import os
import time

print('Bieżący katalog:', os.getcwd())

sciezka = os.getcwd()
plik = 'jakiś plik.txt'
cala_sciezka = os.path.join(sciezka, plik)
print(cala_sciezka)

wzgledna_sciezka = 'wyjscie.txt' #względna ścieżka pliku biorąca aktualne położenie pliku
print('Względna ścieżka:', os.path.abspath(wzgledna_sciezka))

sciezka = r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\6.Operacje wejścia i wyjścia\2.Moduł os.py'
print('\nNazwa pliku:', os.path.basename(sciezka)) #zwraca nazwe pliku z danej ścieżki
print('Ścieżka:', os.path.dirname(sciezka)) #zwraca ścieżkę bez nazwy pliku

print('Czy istnieje?', os.path.exists(sciezka))

if os.path.exists(sciezka):
    print('\nOstatnia modyfikacja pliku:', os.path.getmtime(sciezka))
    print('Ostatnia modyfikacja pliku:', time.localtime(os.path.getmtime(sciezka)))

    print('\nRozmiar:', os.path.getsize(sciezka))

    print('\nCzy plik?', os.path.isfile(sciezka))
    print('Czy folder?', os.path.isdir(sciezka))

    print('\nPoczątek i koniec ścieżki:', os.path.split(sciezka))
    print('Nazwa pliku:', os.path.split(sciezka)[1])

    print('\nDysk oraz scieżka', os.path.splitdrive(sciezka))
    print('Dysk ścieżki:', os.path.splitdrive(sciezka)[0])


print('\n\n############### LAB ################')
dir = input('Podaj ścieżkę do katalogu: ')

if os.path.isdir(dir) == False:
    print('Ścieżka nie prowadzi do katalogu')
else:
    plik = input('Podaj nazwę pliku: ')
    sciezka = os.path.join(dir, plik)
    if os.path.exists(sciezka) == False:
        print('Plik nie istnieje')

    print('\nWłaściwości pliku:')
    print('Data ostatniej modyfikacj:', time.localtime(os.path.getmtime(sciezka)))
    print('Rozmiar:', os.path.getsize(sciezka))
    print('Aktualny katalog:', os.getcwd())
    print('Względna ścieżka:', os.path.relpath(sciezka))

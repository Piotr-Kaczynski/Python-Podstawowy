import os
sciezka = r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt'

file = open(sciezka, 'w') # 'a' -> append pozwala na dopisywanie do pliku a nie pisanie go na nowo

slowo = 'Python'
miasta = ['Gdańsk', 'Paryż', 'Pekin', 'Berlin']

file.write(slowo)
file.write('\n')

for miasto in miasta:
    file.write(miasto + '\n')

file.close()

############### LAB ###############
# adresy_internetowe = []
# line = input('Podaj adres www: ')
# while line != '':
#     adresy_internetowe.append(line)
#     line = input('Podaj adres www: lub wciśnij ENTER ')
# else:
#     nazwa = input('Podaj nazwę pliku w którym zapiszesz adresy: ')
#
# folder = r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki'
# sciezka = os.path.join(folder, nazwa)
# plik = open(sciezka, 'w')
# for adres in adresy_internetowe:
#     plik.write(adres + '\n')
#
# file.close()

#2
sciezka = input('Podaj ścieżkę dostępu do poprzedniego pliku: ')

while os.path.exists(sciezka) == False and os.path.isfile(sciezka) == False:
    sciezka = input('Błędna ścieżka, wprowadź ponownie: ')

adresy_polskie = []
file = open(sciezka, 'r')
dane = [line.strip() for line in file]


for adres in dane:
    if adres[-3:] == '.pl':
        print('adres', adres, 'jest adresem z Polski')
        adresy_polskie.append(adres)
    else:
        print('adres', adres, 'nie jest adresem z Polski')

#3


folder = os.path.dirname(sciezka)
path = os.path.join(folder, 'Adresy_pl')
plik = open(path, 'w')
for adres in adresy_polskie:
    plik.write(adres + '\n')

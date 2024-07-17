#1
file = open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r')

content = file.read()
print(content)

file.close()

#2
with open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r') as file:
    zawartosc = file.read()
    print(zawartosc)

#3
with open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r') as file:
    for line in file:
        print(line)

#4
file = open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r')
for line in file:
    print(line)
file.close()

#5(po określonej liczbie bajtów
file = open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r')
fragment = file.read(4) #liczba bajtów
while fragment:
    print(fragment)
    fragment = file.read(4)
file.close()

#6(funkcja .tell() pokazuje na której pozycji skończyyliśmy
file = open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\tekst.txt', 'r')
fragment = file.read(4) #liczba bajtów
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(4)
file.close()

######## LAB #########
print('\n############### LAB #################')
file = open(r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\data_input\orders.csv', 'r')
dane = [line.strip().split(',') for line in file]

for line in dane:
    if len(line) == 3:
        print('Zamówienie z', line[0], 'na lek', line[1], 'w ilości', line[2])
    else:
        print('Błąd w lini')

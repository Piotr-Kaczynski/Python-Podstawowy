import  sys
# zadania_na_osobe = 0
# try:
#     zadania = 32
#     osoby_str = input('Ile jest osób w zespole: ')
#     osoby = int(osoby_str)
#     zadania_na_osobe = zadania / osoby
# except:
#     print('Coś pooszło nie tak', sys.exc_info()[0]) #sys.exc_info() zwraca opis błędu
# print(zadania_na_osobe)

############# LAB ##############
file_path = r'C:\Users\Dell\Desktop\Programowanie\Python\Podstawowy\Dodatkowe pliki\data_input\orders.csv'

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        try:
            nazwa_apteki = order[0]
            lek = order[1]
            ilosc = int(order[2])
            print('Zamówienie z', nazwa_apteki, 'na', lek, 'w ilości', ilosc)
        except:
            print('Za dużo danych w linijce', line,  sys.exc_info()[0])

print("Processing finished")
import  sys
zadania_na_osobe = 0
try:
    zadania = 32
    osoby_str = input('Ile jest osób w zespole: ')
    osoby = int(osoby_str)
    zadania_na_osobe = zadania / osoby

except ValueError as e: #tworzenie zmiennej 'e' dla błędu którą następnie możemy wyświetlić
    print('Musisz wpisać liczbę: ', e)
except ZeroDivisionError as e:
    print('Nie można wprowadzić zera ', e)
# except:
#     print('Coś pooszło nie tak', sys.exc_info()[0]) #sys.exc_info() zwraca opis błędu
print(zadania_na_osobe)

########### LAB #############
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
        except ValueError as e:
            print('Kolumna trzecia zamówienia zawiera ciąg znaków   Zamówienie:', line)
        except IndexError as e:
            print('Zamówienie zawiera za mało danych   Zamówienie:', line)
        except:
            print('Błąd ogólny')

print("Processing finished")
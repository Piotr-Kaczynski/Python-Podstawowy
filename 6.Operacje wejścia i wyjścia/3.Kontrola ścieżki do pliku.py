import os
import datetime


# while True:
#     nazwa_pliku = input('Podah ścieżke pliku: ')
#     if os.path.exists(nazwa_pliku):
#         break
#     else:
#         print('Zła sciezka')
#
# print('Plik to:', nazwa_pliku)


############ LAB ###############
data_input_catalog = 'C:\\Users\\Dell\\Desktop\\Programowanie\\Python\\Podstawowy\\Dodatkowe pliki\\data_input'
data_output_catalog = 'C:\\Users\\Dell\\Desktop\\Programowanie\\Python\\Podstawowy\\Dodatkowe pliki\\data_output'


dzis = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, dzis.strftime("%Y-%m-%d"))
print(today_output_catalog)


is_input_catalog_ok =  os.path.exists(data_input_catalog) and os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.exists(data_output_catalog) and os.path.isdir(data_output_catalog)
is_today_output_catalog_ok = not os.path.exists(today_output_catalog)

print(is_input_catalog_ok, is_output_catalog_ok, is_today_output_catalog_ok)


if is_today_output_catalog_ok and is_input_catalog_ok and is_output_catalog_ok:
    print('Warunki spełnione')
else:
    print('Błąd')
    if is_today_output_catalog_ok == False:
        print('Dzisiejszy katalog już istnieje')
    elif is_output_catalog_ok == False:
        print('Katalog nie istnieje, lub ścieżka prowadzi do pliku')




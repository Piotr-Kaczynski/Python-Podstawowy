import time
import calendar
print('Aktualny czas:', time.time()) #czas unix'owy. Zegar wystartował z prędkością 1/s w 1.01.1970
print('Aktualny czas:', time.localtime())
print('Aktualny czas:', time.asctime(time.localtime(time.time())))

print(calendar.month(2017, 9, w=4, l=1))
print(calendar.month(2017, 9))
print(calendar.weekday(2017, 9, 29)) #zwraca numer dnia tygodnia(pon - 0, wt - 1, ...)
calendar.setfirstweekday(6) #usatla pierwszy dzień tygodnia
print(calendar.month(2017, 9))
print(calendar.isleap(2020)) #czy przestępny
print(calendar.leapdays(2000, 2017)) #zwraca ilość dni przestępnych w danych latach
print(calendar.calendar(2024)) #wyświetla kalendarz na dany rok

############# LAB ##############
print('############# LAB #############\n')
#2
print('Zadanie 2')
print('Czas Unix Epoche:', time.time())

#3
print('\nZadanie 3')
print('Aktualny czas:', time.asctime(time.localtime(time.time())))

#5
print('\nZadanie 5')
print(calendar.month(2023, 9))

#6
calendar.setfirstweekday(6)

#7
print('\nZadanie 7')
print(calendar.month(1876, 3))

#8
print('\nZadanie 8')
print('Czy 2020 był przestępny:', calendar.isleap(2020))

#9
print('\nZadanie 9')
print(calendar.month(2019, 12))
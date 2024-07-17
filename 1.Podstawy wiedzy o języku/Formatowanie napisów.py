wiadomosc = 'Działanie w toku: %s'
print(wiadomosc % ('usuwanie os.windows'))

wiad2 = 'Plik %s ma rozmiar %d GB'
print(wiad2 % ('Oppenheimer.mp4', 1))

wiad3 = 'Plik %20s ma rozmiar %10f GB' #konstrukcja zostawiająca daną ilość znaków na tekst
print(wiad3 %('Siedem.mp4', 0.9))

wiad4 = 'Przetwarzam plik {0:s}'
print(wiad4.format('virus.bat'))

wiad5 = 'Plik {0:s} waży {1:d} KB' #{pozycja której przypiszemy wartość w fukcji format() : typ}
print(wiad5.format('Auta 4.mp4', 900))

########## LAB ############
helloMessage = 'Hello %s'
print(helloMessage %('Kate'))
print(helloMessage %('Chris'))

helloMessage = "Hello {0:s}!"
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

helloMessage = '%s has %d %s'
print(helloMessage %('Kate', 1, 'animal'))
print(helloMessage %('Chris', 100000, '$'))

helloMessage = '{0:s} has {1:d} {2:s}'
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))

napis = '{0:20s} costs {1:6d}$'
print(napis.format('ICE CREAM', 3))
print(napis.format('Trip to Venice', 119))
print(napis.format('Kawior', 100), '\n29')

napis = '{0:s}  {1:d}'
print(napis.format('Lody', 3))
print(napis.format('Wycieczka', 119))
print(napis.format('Peperoni', 12))
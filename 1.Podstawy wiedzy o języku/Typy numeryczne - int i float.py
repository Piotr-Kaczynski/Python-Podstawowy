import sys
print(sys.maxsize) #9223372036854775807
duza_liczba = 9999999999999999999999999999999999999999 #int
print(type(duza_liczba))
print((duza_liczba + 1)/2) #float 5e+39

print(float('inf')) #nieskończoność
print(-float('inf')) #minus nieskończoność

print(float('inf') > duza_liczba)

############## LAB ################
imie = 'Piotrek'
wiek = 19
dni_w_roku = 365

wiadomosc = '%s ma %d lat, czyli około %d dni'
print(wiadomosc %(imie, wiek, wiek*dni_w_roku))

wiadomosc = '{} ma {} lat, czyli około {} dni'
print(wiadomosc.format(imie, wiek, wiek*dni_w_roku))

print(wiadomosc.format('Chris', 17, 6250))

print(1234567890 // 12345)
print(1234567890 % 12345)


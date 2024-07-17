wyraz = 'Jakiś wyraz :D'
print(wyraz[0])
print(wyraz[2])
print(wyraz[2:7])
print(wyraz[:7])
print(wyraz[7:])
print(wyraz[1:999])
print(wyraz[999:1021001])

wiadomosc = 'Jakaś tam "wiadomość" na potrzeby kursu: Podstawowy'
print(wiadomosc.find(':'))
print(wiadomosc[wiadomosc.find(':')+2:])
print(wiadomosc[wiadomosc.find('"')+1:])

temp = wiadomosc[wiadomosc.find('"')+1:]
print(temp[:temp.find('"')])

############# LAB #############

#2
print('\nZadanie 2')

q = 'THE EYES'
Q = ''
for i in range(len(q)):
    Q += q[i]
    Q += ' '
print(Q)


#3
print('\nZadanie 3')

q = 'a gentelman'
Q = ''
indeksy = [3, 6, 7, 2, 0, 4, 5, 1, 8, 9, 10]

for i in range(len(indeksy)):
    Q += q[indeksy[i]]
print(Q)


#4
print('\nZadanie 4')
q = "THE MORSE CODE"
print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])

#5
print('\nZadanie 5')
line1 = 'Program "Kropka nad i" nadamy o: 22:00'
time1 = line1[line1.find(':')+2:]
print(time1)

indeks1 = line1.find('"')
indeks2 = line1.rfind('"')
title1 = line1[indeks1+1:indeks2] #funkcja rfind() zamiast zmiennej tmp
print(title1, time1)

line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time2 = line2[line2.find(':')+2:]
print(time2)

indeks2_1 = line2.find('"')
indeks2_2 = line2.rfind('"')
title2 = line2[indeks2_1+1:indeks2_2] #funkcja rfind() zamiast zmiennej tmp
print(title2, time2)
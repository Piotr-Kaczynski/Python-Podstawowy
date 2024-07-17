import string
print(string.ascii_letters)
print(string.digits)
cyfry = [i for i in string.digits]

litery = [i for i in string.ascii_lowercase]
LITERY = [i for i in string.ascii_uppercase]

print(cyfry)
print(litery)
print(LITERY)

tekst = 'Jakiś tekst podzielony spacjami'
slowa_tekst = tekst.split(' ') #funkcja .split()
tekst_zlaczony = ' '.join(slowa_tekst) #funkcja .join() -> (łącznik.join(elementy do złączenia)

################ LAB #################

#1
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split('\n')
print(lines)

prawilny_wiersz = ''
for i in range(len(lines)-8):
    prawilny_wiersz += lines[i]
    prawilny_wiersz += '\n'
    prawilny_wiersz += lines[i+8]
    prawilny_wiersz += '\n'
print(prawilny_wiersz)
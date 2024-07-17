########### Funkcje tekstowe #############

tekst = 'Hello world'
print(tekst.endswith('ext'))
print(tekst.endswith('rld'))
print(tekst.islower())
print(tekst.upper())
print(tekst.upper().isupper())
print(tekst.find('llo'))
print(tekst.find('l', 3))
print(tekst.replace('ll', '0'))
print(tekst.split(' '))
liczba_tekst = '100000'
print(liczba_tekst.isdigit()) #sprawdza czy jest liczbą
print(liczba_tekst.isdecimal()) #sprawdza czy jest liczbą po przecinku
print(liczba_tekst.isalpha()) #sprawdza czy składa się tylko z liter
print(liczba_tekst.isalnum()) #sprawdza czy składa się tylko z liter lub cyfr

########### LAB #############

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one', '1'))
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' '))
print(quote.isdigit(), quote.isdecimal(), quote.isalpha(), quote.isalnum())

liczba_tekst = '1000'
print(liczba_tekst + str(1), int(liczba_tekst) + 1)




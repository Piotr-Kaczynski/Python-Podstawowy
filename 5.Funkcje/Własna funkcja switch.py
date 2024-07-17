import math
def dzienTyg(numer):
    nazwy = {
        0: 'poniedziałek',
        1: 'wtorek',
        2: 'środa',
        3: 'czwartek',
        4: 'piątek',
        5: 'sobota',
        6: 'niedziela'
    }

    return nazwy.get(numer, 'błąd')
print(dzienTyg(1))

############## LAB ################

#Zadanie 1
print('\nZadanie 1:')

def element_ciagu_geo(a1=2, q=2, wyraz=2):
    # policz dany wyraz ciągu
    return q**(wyraz-1)*a1
print(element_ciagu_geo(1, 2, 64))


#Zadanie 2

print('\nZadanie 2:')
for i in range(1, 11):
    print(element_ciagu_geo(3, 2, i))


#Zadanie 3
print('\nZadanie 3:')
def iloraz_ciagu(wyraz, nast_wyraz):
    return nast_wyraz / wyraz
print(iloraz_ciagu(12, 24))


#Zadanie 4
print('\nZadanie 4:')
def suma_nWyrazow(a1=2, q=2, n=2):
    if q==1:
        return n*a1
    else:
        return a1*(1-q**n) / (1-q)

print(suma_nWyrazow(2, 3, 4))

import geom
#1
print('\nZadanie1.1')
print(geom.element_ciagu_geo(1, 2, 64))

#2
print('\nZadanie2.1')
for i in range(1, 11):
    print(geom.element_ciagu_geo(3, 2, i))

#3
print('\nZadanie3.1')
print(geom.iloraz_ciagu(12, 24))

#4
print('\nZadanie4.1')
print(geom.suma_nWyrazow(2, 3, 4))




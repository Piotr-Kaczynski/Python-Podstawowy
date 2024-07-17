def wykonaj(akcja, parametr):
    print('akcja', akcja)
    print('parametr', parametr)
    return

wykonaj('skakanie', 'łopata')

def wykonaj_2(akcja, *parametr):
    print('akcja', akcja)
    print('parametr', parametr)
    for element in parametr:
        print('element to:', element)
    return

wykonaj_2('strzelanie', 'grabie', 'uran')

def wykonaj_3(akcja, cos, **parametr):
    print('akcja', akcja)
    print('coś', cos)
    print('parametr', parametr)

    for element in parametr:
        print(element, '=', parametr[element])

    return

wykonaj_3('kup', 'spodnie', rozmiar=38, kolor='szary', typ='eleganckie')


############# LAB #############
def kot():
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return

def misiek():
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return

def gacek():
    txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
    print(txt)
    return

def zwierzeta(*nazwa):
    for zwierze in nazwa:
        if zwierze == 'gacek':
            gacek()
        elif zwierze == 'kot':
            kot()
        elif zwierze == 'misiek':
            misiek()
        else:
            print('błędna nazwa')
    return

zwierzeta('gacek', 'gacek', 'kot', 'misiek', 'kot')


#Zadanie 2
from datetime import  date

def ile_do_sylwestra(*daty):
    for dzis in daty:

        koniec_roku = date(dzis.year, 12, 31)
        ile_zostalo = koniec_roku - dzis
        print('Zostało', ile_zostalo.days, 'dni')

ile_do_sylwestra(date(2024,3,3), date(2018, 10, 19) )



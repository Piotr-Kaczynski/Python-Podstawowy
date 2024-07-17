from datetime import  date

def ile_do_sylwestra(rok=date.today().year, miesiac=date.today().month, dzien=date.today().month): #dopisanie wartości domyślnej dla 'dzień'
    dzisiaj = date(rok, miesiac, dzien)
    rok = dzisiaj.year
    koniec_roku = date(rok, 12, 31)
    ile_zostalo = koniec_roku - dzisiaj
    return ile_zostalo.days

ile_do_sylwestra(2024, 12, 30)
ile_do_sylwestra(rok=2029, miesiac=2, dzien=1)
ile_do_sylwestra(miesiac=9, rok=3082, dzien=18)
ile_do_sylwestra(2024, 9)
ile_do_sylwestra()

print('Zostało:', ile_do_sylwestra(1976, 8, 17), 'dni')



########## LAB ###########
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

def zwierze(nazwa=''):
    if nazwa == 'gacek':
        return gacek()
    elif nazwa == 'misiek':
        return misiek()
    elif nazwa == 'kot':
        return kot()
    elif nazwa == '':
        return print('podaj poprawny parametr')
    else:
        print('Zwierze:', nazwa, 'nie występuje')

# zwierze('misiek')
# zwierze('krowa')
# zwierze('gacek')
# zwierze()


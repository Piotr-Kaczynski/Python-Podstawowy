from datetime import  date
from datetime import timedelta

def dzienRoboczy():
    dzis = date.today()

    if dzis.weekday() == 5:
        dzien_pracujacy = dzis + timedelta(days=2)
    elif dzis.weekday() == 6:
        dzien_pracujacy = dzis + timedelta(days=1)
    else:
        dzien_pracujacy = dzis

    print('Dziś:', dzis, ' dzień pracujący:', dzien_pracujacy)

dzienRoboczy()


############ LAB ##############

def ile_do_sylwestra():
    dzisiaj = date.today()
    rok = dzisiaj.year
    koniec_roku = date(rok, 12, 31)
    ile_zostalo = koniec_roku - dzisiaj
    print('Sylwester za:', ile_zostalo.days, 'dni')
    return 
ile_do_sylwestra()
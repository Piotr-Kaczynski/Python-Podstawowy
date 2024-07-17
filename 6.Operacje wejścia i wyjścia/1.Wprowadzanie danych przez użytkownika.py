# nazwa_pliku = input('Podaj nazwe pliku: ')
# # print('Plik nazywa się: %s' %(nazwa_pliku))

#
# while True:
#
#     rozmiar_pliku_str = input('Podaj rozmiar pliku: ')
#     if rozmiar_pliku_str.isdecimal():
#         rozmiar_pliku_int = int(rozmiar_pliku_str)
#         break
#     else:
#         print('Złe dane')
# print('Rozmiar pliku to: %d' %(rozmiar_pliku_int)) #można podać tylko liczbę
#
#


########## LAB ###########
def isNum(x):
    if x[0] == '-':
        return x[1:].isdigit()
    return x.isdigit()

a_str = input('a:')
b_str = input('b:')
c_str = input('c:')

if isNum(a_str) and isNum(b_str) and isNum(c_str):
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0:
        print('a=0 opisuje funkcje liniową')

    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('Brak rozwiązań')

        elif delta == 0:
            x = -b/(2*a)
            print('Jedno rozwiązanie:', x)
        else:
            x1 = (-b - delta**0.5) / (2 * a)
            x2 = (-b + delta**0.5) / (2 * a)
            print('Dwa rozwiązania:', x1, x2)
else:
    print('współczynniki muszą być liczbami całkowitymi')





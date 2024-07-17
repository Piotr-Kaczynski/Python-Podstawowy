from random import *
#1
mini = 1
maxi = 6

rzut = randint(mini, maxi)

if rzut == 1:
    print('   \n * \n   ')
elif rzut == 2:
    print('*  \n   \n  *')
elif rzut == 3:
    print('*  \n * \n  *')
elif rzut == 4:
    print(print('* *\n   \n* *'))
elif rzut == 5:
    print('* *\n * \n* *')
elif rzut == 6:
    print('***\n   \n***')

#2
rzuty = []
for i in range(5):
    rzuty.append(randint(mini, maxi))

rzuty.sort()
print(rzuty)
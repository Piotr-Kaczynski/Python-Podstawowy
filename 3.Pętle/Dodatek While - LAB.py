############## LAB #################
tekst_3 = 'United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.'

#1
print('Zadanie 1:')

initialCapital = 20000
opro = 0.03
czasMaks = 10
rok = 1
ile = initialCapital
while rok <= czasMaks:
    ile = (1+opro)*ile
    print('W roku', rok, 'bedzie miał', ile)
    rok += 1
else:
    print('W sumie zarobił:', ile-initialCapital)


#2
print('\nZadanie 2:')
number = 20730906
tmp = number
suma = 0
while tmp > 0:
    suma += tmp % 10
    tmp //= 10
print(suma)

#3
print('\nZadanie 3:')

slowa = tekst_3.split(' ')
i = 0
ile = 0
while i != len(slowa):
    if len(slowa[i]) > 6:
        ile += 1
    i += 1
print(ile)

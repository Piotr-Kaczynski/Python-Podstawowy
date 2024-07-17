weekend = True
temp = 25
zadania = 'pranie'

czy_szczescie = weekend and temp >= 20 and zadania == ''
print('Czy szczęśliwy: ', czy_szczescie)

czy_szczescie = weekend and temp <= 10 and zadania != ''
print('Czy szczęśliwy: ', czy_szczescie)

czy_szczescie = weekend and temp >= 20 and zadania == '' \
or not weekend and temp < 20 and zadania != ''
print('Czy szczęśliwy: ', czy_szczescie)

# list != []         lub    not list == []
# not A and not B    lub    not(A or B)

############## LAB #################
isAutomaticMode = False
is80percentLight = True
isDirectLight = False
isRainy = True


turnLightsOn = isAutomaticMode and (not is80percentLight or isDirectLight or isRainy)
 
print('\nTryb automatyczny:', isAutomaticMode)
print('Dobre naświetlenie:', is80percentLight)
print('Czy słońce jest nisko:', isDirectLight)
print('Czy pada:', isRainy)
print('\nCzy włączyć światła: ', turnLightsOn)
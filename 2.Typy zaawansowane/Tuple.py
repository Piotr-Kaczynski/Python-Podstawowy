Tax = (0, 4, 9, 11)

print(Tax)
print(Tax[0])

print(Tax.index(9)) #index danego elementu
print(Tax.count(11)) #zlicza wystąpienia elementu
print(max(Tax)) #zwraca maksymalną wartość tupla

#insert(), append(), sort() zwracają error
Taxlist = list(Tax) #konwertuje tupla do listy
print(Taxlist)
Taxlist.append(30)

New_Tax = tuple(Taxlist)
print(Taxlist)
print(New_Tax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

a = 1
b = 10
print('a =', a, '\tb =', b)

#zamiana wartości zmiennych z użyciem zmiennej tmp
# tmp = a
# a = b
# b = tmp
print('a =', a, '\tb =', b)

(a, b) = (b, a)
print('a =', a, '\tb =', b)

############## LAB ################
print('\n############## LAB ################')
#1
marketing = ['loyality program', 'client promotion', 'market reaserch']
print(marketing)

#2
marketing.append('public relations')
print(marketing)

#3
print(marketing[3])

#4
marketing.insert(2, 'investor relations')
print(marketing)

#5
emailMarketing = marketing.copy()
print(emailMarketing)

#6
emailMarketing.sort()
print(emailMarketing)

#7
internalEmails = ['internal comunication']
print(emailMarketing, internalEmails)

#8
emailMarketing.extend(internalEmails)
print(emailMarketing)

#9
emailMarketing_t = tuple(emailMarketing)
print(emailMarketing_t)





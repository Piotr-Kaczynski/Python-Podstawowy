################# LAB ####################

data = ['Error:File cannot be open', 'Error:No free space on disk', 'Error:File missing', 'Warning:Internet connection lost', 'Error:Access denied']

#1
for i in data:
    print(i.upper())

elements = []
#2
for i in data:
    elements.append(i.split(':'))
print('')

for j in elements:
    print(j[0].upper(), j[1])

#3
print('')
for n in elements:
    if n[0] == 'Error':
        print(n[1].upper())
    else:
        print(n[1])

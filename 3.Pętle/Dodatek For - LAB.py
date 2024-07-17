###################### LAB #######################
#1
print('Zadanie 1')
fibonaci = [1, 1]
for i in range(18):
    z = fibonaci[i] + fibonaci[i+1]
    fibonaci.append(z)
print(fibonaci)

#2
print('\nZadanie 2')
tekst = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn't do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it's an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can't.'''

data2 = tekst.replace('\n', ' ').split(' ')

for i in range(len(data2)):
    if 'p' in data2[i].lower():
        print(data2[i])

#3
print('\nZadanie 3')
dictionary = {'A': '80%-100%', 'B': '60%-80%', 'C': '50-60%', 'D': 'less than 50%'}

for key in dictionary:
    print(key, '-', dictionary[key])


#4
print('\nZadanie 4')
wordDictionary = {}
for word in data2:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word] + 1
    else:
        wordDictionary.setdefault(word, 1)


for key in wordDictionary.keys():
    print(key, '-', wordDictionary[key])



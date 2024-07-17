menu = 'Co mam zrobić?\n1-Salto\n2-Obiad\n3-Lekcje pytona\n---------------\n0-Przerwij skrypt'

while True:
    print(menu)
    wybor = input()
    if wybor == '1':
        print("Function SALTO not implemented\nPress ENTER")
        input()
        continue

    if wybor == '2':
        print("Function OBIAD not implemented\nPress ENTER")
        input()
        continue

    if wybor == '3':
        print("Siadaj i się ucz pytona!\nPress ENTER")
        input()
        continue
    if wybor == '0':
        break
    print('Wybierz odpowiednią opcje!')

#Катарина Андрич ИУ7 - 16Б
#Провераем ввод
def timenum(list0):
    if not list0[0] == '-2' or not list0[0] == '-1':
        while int(list0[0]) < 0:
            print('Error. Invalid input.')
            list0 = list(input('Try again: ').split())
        while int(list0[2]) < 1 or int(list0[2]) > 127:
            print('Error. Invalid input.')
            list0 = list(input('Try again: ').split())
        return list0
#Фиксируем слова ‘on’ и ‘off’
def on(list0):
    if list0[1] == 'on' or list0[1] == 'On' or list0[1] == 'oN':
            list0.remove(list0[1])
            list0.insert(1,'ON')
    return list0

def off(list0):
    if list0[1] == 'off' or list0[1] == 'Off' or list0[1] == 'OFf' or list0[1] == 'OfF' or list0[1] == 'oFF':
            list0.remove(list0[1])
            list0.insert(1,'OFF')
    return(list0)
#Вводим строку
red = list(input('Line: ').split())
#Провераем ввод
red = timenum(red)
Music = []
notelist = []
#Добавляем строку в массив 
while not red[0] == '-2':
    if not red[0] == '-1':
        red = timenum(red)
        on(red)
        off(red)
        if red[2] not in notelist:
            notelist.append(red[2])
    stred = ' '.join(map(str,red))
    Music.append(stred)
    red.clear()
    red = list(input('Line: ').split())
Music.append('-2')


Final = []
A = []
E = []
P = []
#Проверяем каждую программу, кроме последней
while '-1' in Music:
    while not Music[0] == '-1':
        f = Music[0].split()
        A.append(Music[0])
        Music.remove(Music[0])
    for d in range(len(notelist)):
        for a in range(len(A)):
            e = A[a].split()
            if notelist[d] == e[2]:                             #Составляем список всех функций одной музыкальной ноты
                E.append(A[a])
        for b in range(len(E)):                                 #проверяем все условия, которые были предоставлены
            if not b == (len(E)-1):
                firstline = E[b].split()
                nextline = E[b+1].split()
                if firstline[1] == nextline[1] == 'ON':
                    new = str(int(nextline[0])-1) + ' ' + 'OFF' + ' ' + notelist[d]
                    E.insert((b+1),new)
                if firstline[1] == nextline[1] == 'OFF':
                    E.remove(E[b])
                if firstline[0] == nextline[0] and firstline[1] == 'OFF' and nextline[1] == 'ON':
                    w = str(int(firstline[0])-1) + ' ' + 'OFF' + ' ' + notelist[d]
                    E.insert(b,w)
                    E.remove(E[b+1])
        for s in range(len(E)):
            if not s > (len(E)-2):
                firstline = E[s].split()
                nextline = E[s+1].split()
                if firstline[0] == nextline[0] and firstline[1] == 'ON' and nextline[1] == 'OFF':
                    E.remove(E[s+1])
                    E.remove(E[s+1])

        P.extend(E)
        E.clear()
    for i in range(len(P)):                                             #Сортируем все ноты в порядке возрастания по времени
        for j in range(i,len(P)-1):
            if int((P[i].split())[0])>int((P[j].split())[0]):
                P[i],P[j] = P[j],P[i]        
    Final.extend(P)                                                     #Добавляем массив в главный массив
    P.clear()
    Final.append('-1')
    A.clear()
    Music.remove(Music[0])
#Проверяем последную программу
while '-2' in Music:
    while not Music[0] == '-2':
        A.append(Music[0])
        Music.remove(Music[0])
    for d in range(len(notelist)):
        for a in range(len(A)):
            e = A[a].split()
            if notelist[d] == e[2]:
                E.append(A[a])
        for b in range(len(E)):                                             #проверяем все условия, которые были предоставлены
            if not b == (len(E)-1):
                firstline = E[b].split()
                nextline = E[b+1].split()
                if firstline[1] == nextline[1] == 'ON':
                    new = str(int(nextline[0])-1) + ' ' + 'OFF' + ' ' + notelist[d]
                    E.insert((b+1),new)
                if firstline[1] == nextline[1] == 'OFF':
                    E.remove(E[b])
                if firstline[0] == nextline[0] and firstline[1] == 'OFF' and nextline[1] == 'ON':
                    w = str(int(firstline[0])-1) + ' ' + 'OFF' + ' ' + notelist[d]
                    E.insert(b,w)
                    E.remove(E[b+1])
        for s in range(len(E)):
            if not s > (len(E)-2):
                firstline = E[s].split()
                nextline = E[s+1].split()
                if firstline[0] == nextline[0] and firstline[1] == 'ON' and nextline[1] == 'OFF':
                    E.remove(E[s+1])
                    E.remove(E[s+1])
    for i in range(len(E)):                                         #Сортируем все ноты в порядке возрастания по времени
        for j in range(i,len(E)-1):
            if int((E[i].split())[0])>int((E[j].split())[0]):
                E[i],E[j] = E[j],E[i]
    Music.remove(Music[0])
Final.extend(E)                                     #Добавляем массив в главный массив
Final.append('-2')
print()
print('OUTPUT: ')
for v in range(len(Final)):
    print(Final[v])                             #Печатаем решение

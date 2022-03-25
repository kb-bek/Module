#1.Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл.

import my_module

#2.Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] и вытащите 4 рандомных имени оттуда и сохраните в другой список.

# import random
l = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
lst  = []
for i in range(4):
    lst.append(random.choice(l))
print(lst)


#3.Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.


import sys
print(sys.platform)

#4.Через терминал передайте Python несколько аргументов, а затем выведите их на экран.
i = input('Аргумент:')
def print_args(a):
    print(eval(a))

print_args(i

#5.Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
from random import randint
from os import system


for i in range(5):
    r = randint(1,10)
    system(f'touch /home/kuba/Рабочий стол/DFG/{r}.txt')




#6.Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
team1 = []
team2 = []
team3 = []
team4 = []
count = 1
len_team = len(names)//4

while names != []:
    name = random.choice(names)
    if count <= len_team:
        team1.append(name)
        names.remove(name)

    elif count <= len_team * 2:
        team2.append(name)
        names.remove(name)

    elif count <= len_team * 3:
        team3.append(name)
        names.remove(name)

    else:
        team4.append(name)
        names.remove(name)

    count += 1


print(team1)
print(team2)
print(team3)
print(team4)
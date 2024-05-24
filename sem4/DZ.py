""" Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств. """

""" import random

n = int(input('Введите кол-во элементов 1-го множеста: '))
m = int(input('Введите кол-во элементов 2-го множеста: '))
user_list1 = []
user_list2 = []
for i in range(0,n):                                   #рандомно заполняем список целыми числами
    user_list1.append(random.randint(0,20))
for i in range(0,m):                                   #рандомно заполняем список целыми числами
    user_list2.append(random.randint(0,20))

print(user_list1)
print(user_list2)

print(set(user_list1)&set(user_list2)) """


#------------------------------------------------------------------------------------------------
""" Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки. """

import random
n = int(input('Введите кол-во кустов на грядке: '))
user_list = []
for i in range(0,n):                                   #рандомно заполняем список целыми числами
    user_list.append(random.randint(0,10))
print(user_list)

max = 0
for i in range(n-2):
    if user_list[i]+user_list[i+1]+user_list[i+2] > max:
        max = user_list[i]+user_list[i+1]+user_list[i+2]
    if user_list[n-2]+user_list[n-1]+user_list[0] > max:
        max = user_list[n-2]+user_list[n-1]+user_list[0]      
print(max)

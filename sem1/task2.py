# Задача №3. 
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
n1= int(input())
n2= int(input())
n3= int(input())
if (n1+n2+n3)%2 == 0:
    print((n1+n2+n3)//2)
else :
    print((n1+n2+n3)//2+1)

#или
# print((n1+n2+n3+1)//2)
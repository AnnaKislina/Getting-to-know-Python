# ДОМАШНЕЕ ЗАДАНИЕ

# Задача 2: Найдите сумму цифр трехзначного числа. 
# n = int(input())
# sum = 0
# while n > 0:
#     sum = sum + n % 10
#     n = n // 10
# print(sum)
# ------------------------------------------------

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# s = int(input())
# x = int(s / 6)
# print(f"Петя {x}; Катя {4*x}; Сережа {x}")
# ------------------------------------------------

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется  написать
# программу, которая проверяет счастливость билета
# n = int(input())
# n1= n // 1000
# n2= n % 1000
# sum1=0
# sum2=0
# while n1 > 0:
#     sum1 = sum1 + n1 % 10
#     n1 = n1 // 10
#     sum2 = sum2 + n2 % 10
#     n2 = n2 // 10
# if sum1 == sum2:
#     print("YES")
# else:
#     print("NO")
# ------------------------------------------------

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
n = int(input())
m = int(input())
k = int(input())
if n % k == 0 or m % k == 0:
    print("Yes")
else:
    print("No")



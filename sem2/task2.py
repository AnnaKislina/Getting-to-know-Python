"""
Задача №11. 
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 """
# 0 1 1 2 3 5 8 13
# 1 2 3 4 5 6 7 8

n = int(input('Введите натуральное число: '))
n0=0
n1=0
n2=1
i=2

while n0<n:
    n0 = n1 + n2
    n1 = n2
    n2= n0
    i +=1
    if n0 > n:
        i = -1
print(i)
""" Задача №19. 
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально. """

user_list = [1, 2, 3, 4, 5] 
k = 3
res_list=[]
res_list.extend(user_list[k:len(user_list)])
res_list.extend(user_list[0:k])
print(res_list)


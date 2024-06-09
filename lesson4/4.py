""" В списке хранятся числа. Нужно выбрать только чётные числа 
и составить список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)] """

""" data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out) """

""" def select(f, col):
    return [f(x) for x in col] #возвращает список к которому применили функцию х
def where(f, col):
    return [x for x in col if f(x)] #возаращает ттолько те значения которые прошли провеерку f(x)
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res) """
#-----------------------------------------------------------------

"""   C клавиатуры вводится некий набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как
превратить list строк в list чисел? """
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
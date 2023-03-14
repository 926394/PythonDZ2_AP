'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)


'''
n = int (input('Здравствуйте! Введите количество элементов --> '))   
colors0 = list()
for i in range(n):
    colors0.append(i+1)

num_min = int(input('Введите min элемент: '))
max_min = int(input('Введите max элемент: '))
for i in range(len(colors0)):
    if num_min <= colors0[i] <= max_min:
        print(i)


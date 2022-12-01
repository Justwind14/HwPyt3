# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
# (максимальное значение у числа 1.2 , минимальное у 10.01)

import random
n = int(input())
some_list = [round(random.randint(1,19) + random.random(),2) for _ in range(n)]
print(some_list, end = '')
some_list2 = [i%1 for i in some_list if i%1 != 0]
print(' =>', round((max(some_list2) - min(some_list2)), 2))
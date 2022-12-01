# 1. Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input())
some_list = [random.randint(-n, n) for _ in range(n)]
print(some_list, ' -> на нечётных позициях элементы: ', end='')
sum = 0
for i in range(1, n, 2):
    sum += some_list[i]
    print(some_list[i], end=', ')
print('ответ: ', sum)

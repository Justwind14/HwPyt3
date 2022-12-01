# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input())
some_list1 = [random.randint(-n, n) for _ in range(n)]
print(some_list1, end = '')
print(' => ',[some_list1[i] * some_list1[-1 * (1 + i)] for i in range(0, (n + 1) //2)])
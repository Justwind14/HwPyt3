# 4. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число:'))
new_str = ' ' 
while n > 0:  
    new_str = new_str + str(n % 2)  
    n = n // 2
for i in reversed(new_str):
    print(i, end = '')
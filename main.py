from random import randint

# Задача №36. Создайте список из случайных чисел. Найдите количество различных элементов в нем.

rand_list = [(int(randint(1, 10))) for _ in range(int(input()))]

print(rand_list)
print(len(set(rand_list)))





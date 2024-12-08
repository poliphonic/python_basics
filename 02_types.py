#!/usr/bin/env python3

# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.

import random
seq = [True, 5j, {'Аргентина': 'Ямайка', 5: 0}, 5.0, 5, [5, 0],
       random.choice, random, None, range(10),
       {'Аргентина', 'Ямайка', 5, 0}, 'None', (5, 0), type(1)]
print(*[type(i) for i in seq], sep='\n')

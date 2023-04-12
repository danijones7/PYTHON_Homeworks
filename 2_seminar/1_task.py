# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 => 2

import random
N = int(input("Введите количество монеток: "))
count0 = 0
count1 = 0
for i in range(N):
    monetka = random.randint(0, 1)
    print(monetka) 
    if monetka == 0:
        count0 +=1
    else:
        count1 +=1
if count0 < count1:
    print(f"Минимальное количество монет, которые нужно перевернуть: {count0}")
else:
    print(f"Минимальное количество монет, которые нужно перевернуть: {count1}")